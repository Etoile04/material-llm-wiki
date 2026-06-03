#!/usr/bin/env python3
"""
Zotero MCP 迁移测试脚本

测试所有迁移后的功能
"""

import sys
import os
import json
import time
from pathlib import Path

# 添加技能路径
SKILL_ROOT = Path("/Users/lwj04/.openclaw/skills")
sys.path.insert(0, str(SKILL_ROOT / "zotero-workflow-skills" / "zotero-mcp"))

from zotero_mcp_unified import ZoteroMCPClient


def print_section(title):
    """打印分节标题"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def test_1_connection():
    """测试 1: 连接测试"""
    print_section("测试 1: MCP 连接测试")

    client = ZoteroMCPClient()
    result = client.test_connection()

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("success"):
        print(f"✅ 连接成功！")
        print(f"   端点: {result['endpoint']}")
        print(f"   收藏夹数量: {result['collections_count']}")
        return True
    else:
        print(f"❌ 连接失败: {result.get('error')}")
        return False


def test_2_keyword_search():
    """测试 2: 关键词搜索"""
    print_section("测试 2: 关键词搜索")

    client = ZoteroMCPClient()
    result = client.search_library(query="agent memory", limit=3)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if "data" in result:
        results = result["data"].get("results", [])
        print(f"\n✅ 搜索成功！")
        print(f"   找到 {len(results)} 篇文献")
        print(f"   搜索时间: {result['data'].get('searchTime', 'N/A')}")
        return True
    else:
        print(f"\n❌ 搜索失败: {result.get('error')}")
        return False


def test_3_semantic_search():
    """测试 3: 语义搜索"""
    print_section("测试 3: 语义搜索")

    client = ZoteroMCPClient()
    result = client.semantic_search(
        query="AI agent memory and self-improvement",
        limit=3
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if "data" in result:
        data = result.get("data", [])
        print(f"\n✅ 语义搜索成功！")
        print(f"   找到 {len(data)} 篇相关文献")
        if data:
            print(f"   最高相似度: {data[0].get('score', 0):.3f}")
        return True
    else:
        print(f"\n❌ 语义搜索失败: {result.get('error')}")
        return False


def test_4_get_item_details():
    """测试 4: 获取文章详情"""
    print_section("测试 4: 获取文章详情")

    client = ZoteroMCPClient()

    # 先搜索一篇文章
    search_result = client.search_library(query="agent memory", limit=1)

    if "data" not in search_result:
        print("❌ 搜索失败，无法测试详情获取")
        return False

    papers = search_result["data"].get("results", [])
    if not papers:
        print("❌ 未找到文献，无法测试详情获取")
        return False

    item_key = papers[0].get("key")
    print(f"获取文章详情: {item_key}\n")

    result = client.get_item_details(item_key=item_key)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if "data" in result:
        item = result["data"]
        print(f"\n✅ 获取详情成功！")
        print(f"   标题: {item.get('title', 'N/A')[:50]}...")
        print(f"   作者数量: {len(item.get('creators', []))}")
        print(f"   标签数量: {len(item.get('tags', []))}")
        return True
    else:
        print(f"\n❌ 获取详情失败: {result.get('error')}")
        return False


def test_5_collections():
    """测试 5: 收藏夹管理"""
    print_section("测试 5: 收藏夹管理")

    client = ZoteroMCPClient()
    result = client.get_collections()

    print(json.dumps(result, indent=2, ensure_ascii=False) if isinstance(result, (dict, list)) else str(result))

    # Handle both dict{"data": [...]} and direct list responses
    if isinstance(result, list):
        collections = result
    elif isinstance(result, dict) and "data" in result:
        data = result.get("data", [])
        if isinstance(data, list):
            collections = data
        else:
            collections = data.get("collections", [])
    else:
        print(f"\n❌ 获取收藏夹失败: {result}")
        return False

    print(f"\n✅ 获取收藏夹成功！")
    print(f"   收藏夹数量: {len(collections)}")

    if collections:
        print(f"\n前 5 个收藏夹:")
        for coll in collections[:5]:
            name = coll.get("name", "N/A") if isinstance(coll, dict) else coll
            print(f"   - {name}")
    return True


def test_6_semantic_status():
    """测试 6: 语义搜索状态"""
    print_section("测试 6: 语义搜索状态")

    client = ZoteroMCPClient()
    result = client.semantic_status()

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if "data" in result:
        status = result["data"]
        print(f"\n✅ 获取语义搜索状态成功！")
        print(f"   索引文章数: {status.get('index_items', 'N/A')}")
        print(f"   索引大小: {status.get('index_size', 'N/A')}")
        return True
    else:
        print(f"\n❌ 获取语义搜索状态失败: {result.get('error')}")
        return False


def test_7_workflow():
    """测试 7: 完整工作流"""
    print_section("测试 7: 完整工作流")

    client = ZoteroMCPClient()

    # 步骤 1: 搜索
    print("步骤 1: 搜索文献...")
    search_result = client.search_library(query="agent memory", limit=5)

    if "data" not in search_result:
        print("❌ 搜索失败")
        return False

    papers = search_result["data"].get("results", [])
    print(f"   ✅ 找到 {len(papers)} 篇文献")

    # 步骤 2: 获取详情
    print("\n步骤 2: 获取文章详情...")
    item_key = papers[0].get("key")
    detail_result = client.get_item_details(item_key=item_key)

    if "data" not in detail_result:
        print("❌ 获取详情失败")
        return False

    item = detail_result["data"]
    print(f"   ✅ 获取详情: {item.get('title', 'N/A')[:50]}...")

    # 步骤 3: 语义搜索相似文章
    print("\n步骤 3: 查找相似文章...")
    similar_result = client.find_similar(item_key=item_key, limit=3)

    if "data" not in similar_result:
        print("❌ 查找相似文章失败")
        return False

    similar = similar_result.get("data", [])
    print(f"   ✅ 找到 {len(similar)} 篇相似文章")

    print(f"\n✅ 完整工作流测试成功！")
    return True


def run_all_tests():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("  Zotero MCP 迁移测试套件")
    print("=" * 60)

    tests = [
        ("连接测试", test_1_connection),
        ("关键词搜索", test_2_keyword_search),
        ("语义搜索", test_3_semantic_search),
        ("获取文章详情", test_4_get_item_details),
        ("收藏夹管理", test_5_collections),
        ("语义搜索状态", test_6_semantic_status),
        ("完整工作流", test_7_workflow),
    ]

    results = []
    start_time = time.time()

    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ 测试失败: {test_name}")
            print(f"   错误: {str(e)}")
            results.append((test_name, False))

        time.sleep(1)  # 避免请求过快

    # 汇总结果
    elapsed = time.time() - start_time
    passed = sum(1 for _, result in results if result)
    total = len(results)

    print_section("测试汇总")
    print(f"总耗时: {elapsed:.2f} 秒")
    print(f"通过: {passed}/{total}")
    print(f"失败: {total - passed}/{total}")

    print(f"\n详细结果:")
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {test_name}: {status}")

    if passed == total:
        print(f"\n{'=' * 60}")
        print(f"  🎉 所有测试通过！")
        print(f"{'=' * 60}\n")
        return True
    else:
        print(f"\n{'=' * 60}")
        print(f"  ⚠️  {total - passed} 个测试失败")
        print(f"{'=' * 60}\n")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
