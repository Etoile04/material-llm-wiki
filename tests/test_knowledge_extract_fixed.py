#!/usr/bin/env python3
"""
knowledge-extract-fixed 迁移测试脚本

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
sys.path.insert(0, str(SKILL_ROOT / "zotero-workflow-skills" / "knowledge-extract-fixed"))

from zotero_mcp_unified import ZoteroMCPClient
from knowledge_extract_fixed_skill import KnowledgeExtractorFixed


def print_section(title):
    """打印分节标题"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def test_1_basic_extraction():
    """测试 1: 基本知识提取"""
    print_section("测试 1: 基本知识提取")

    # 创建测试数据
    test_papers = [
        {
            "zotero_key": "TEST001",
            "key": "TEST001",
            "title": "Thermal conductivity of U-Mo alloy",
            "creators": [{"firstName": "John", "lastName": "Doe"}],
            "tags": ["U-Mo", "fuel", "thermal"]
        }
    ]

    # 创建提取器
    extractor = KnowledgeExtractorFixed()

    # 执行提取
    result = extractor.extract_from_papers(
        papers=test_papers,
        extract_numerical=False,
        extract_relations=False,
        confidence_threshold=0.6
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("status") == "success":
        knowledge = result.get("knowledge", [])
        print(f"\n✅ 基本提取成功！")
        print(f"   文献数: {result['stats']['total_papers']}")
        if knowledge:
            materials = knowledge[0].get("extracted_entities", {}).get("materials", [])
            print(f"   提取材料: {materials}")
        return True
    else:
        print(f"\n❌ 基本提取失败")
        return False


def test_2_numerical_extraction():
    """测试 2: 数值属性提取"""
    print_section("测试 2: 数值属性提取")

    # 创建测试数据
    test_papers = [
        {
            "zotero_key": "TEST002",
            "key": "TEST002",
            "title": "Density and thermal conductivity measurements",
            "creators": [{"firstName": "Jane", "lastName": "Smith"}],
            "tags": ["density", "thermal"]
        }
    ]

    # 创建提取器
    extractor = KnowledgeExtractorFixed()

    # 执行提取（包含数值）
    result = extractor.extract_from_papers(
        papers=test_papers,
        extract_numerical=True,
        extract_relations=False,
        confidence_threshold=0.6
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("status") == "success":
        stats = result.get("stats", {})
        print(f"\n✅ 数值提取成功！")
        print(f"   提取数值: {stats.get('extracted_values', 0)}")
        print(f"   平均置信度: {stats.get('avg_confidence', 0)}")

        # 检查数值
        knowledge = result.get("knowledge", [])
        if knowledge:
            values = knowledge[0].get("extracted_entities", {}).get("values", {})
            if values:
                print(f"\n   提取的数值:")
                for prop, val in values.items():
                    print(f"     {prop}: {val.get('value', 'N/A')} {val.get('unit', '')}")

        return True
    else:
        print(f"\n❌ 数值提取失败")
        return False


def test_3_relation_extraction():
    """测试 3: 关系提取"""
    print_section("测试 3: 关系提取")

    # 创建测试数据
    test_papers = [
        {
            "zotero_key": "TEST003",
            "key": "TEST003",
            "title": "U-Mo alloy properties and swelling behavior",
            "creators": [{"firstName": "Bob", "lastName": "Johnson"}],
            "tags": ["U-Mo", "swelling", "properties"]
        }
    ]

    # 创建提取器
    extractor = KnowledgeExtractorFixed()

    # 执行提取（包含关系）
    result = extractor.extract_from_papers(
        papers=test_papers,
        extract_numerical=False,
        extract_relations=True,
        confidence_threshold=0.6
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("status") == "success":
        stats = result.get("stats", {})
        print(f"\n✅ 关系提取成功！")
        print(f"   提取关系: {stats.get('extracted_relations', 0)}")

        # 检查关系
        knowledge = result.get("knowledge", [])
        if knowledge:
            relations = knowledge[0].get("relations", [])
            if relations:
                print(f"\n   提取的关系:")
                for rel in relations[:5]:
                    print(f"     {rel['source']} -> {rel['relation']} -> {rel['target']}")

        return True
    else:
        print(f"\n❌ 关系提取失败")
        return False


def test_4_full_extraction():
    """测试 4: 完整提取（数值 + 关系）"""
    print_section("测试 4: 完整提取")

    # 创建测试数据
    test_papers = [
        {
            "zotero_key": "TEST004",
            "key": "TEST004",
            "title": "Comprehensive study of U-10Mo fuel properties",
            "creators": [{"firstName": "Alice", "lastName": "Williams"}],
            "tags": ["U-10Mo", "fuel", "properties"]
        }
    ]

    # 创建提取器
    extractor = KnowledgeExtractorFixed()

    # 执行完整提取
    result = extractor.extract_from_papers(
        papers=test_papers,
        extract_numerical=True,
        extract_relations=True,
        confidence_threshold=0.6
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("status") == "success":
        stats = result.get("stats", {})
        print(f"\n✅ 完整提取成功！")
        print(f"   总文献数: {stats.get('total_papers', 0)}")
        print(f"   提取材料: {stats.get('total_materials', 0)}")
        print(f"   提取属性: {stats.get('total_properties', 0)}")
        print(f"   提取数值: {stats.get('extracted_values', 0)}")
        print(f"   提取关系: {stats.get('extracted_relations', 0)}")
        print(f"   平均置信度: {stats.get('avg_confidence', 0)}")
        return True
    else:
        print(f"\n❌ 完整提取失败")
        return False


def test_5_confidence_threshold():
    """测试 5: 置信度阈值过滤"""
    print_section("测试 5: 置信度阈值过滤")

    # 创建测试数据
    test_papers = [
        {
            "zotero_key": "TEST005",
            "key": "TEST005",
            "title": "U-Mo alloy properties study",
            "creators": [{"firstName": "Charlie", "lastName": "Brown"}],
            "tags": ["U-Mo", "properties"]
        }
    ]

    # 创建提取器
    extractor = KnowledgeExtractorFixed()

    # 使用高阈值
    result = extractor.extract_from_papers(
        papers=test_papers,
        extract_numerical=True,
        extract_relations=True,
        confidence_threshold=0.9
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("status") == "success":
        stats = result.get("stats", {})
        print(f"\n✅ 阈值过滤成功！")
        print(f"   阈值: 0.9")
        print(f"   提取数值: {stats.get('extracted_values', 0)}")
        print(f"   提取关系: {stats.get('extracted_relations', 0)}")

        # 与低阈值对比
        result_low = extractor.extract_from_papers(
            papers=test_papers,
            extract_numerical=True,
            extract_relations=True,
            confidence_threshold=0.5
        )

        stats_low = result_low.get("stats", {})
        print(f"\n   对比（阈值 0.5）:")
        print(f"   提取数值: {stats_low.get('extracted_values', 0)}")
        print(f"   提取关系: {stats_low.get('extracted_relations', 0)}")

        return True
    else:
        print(f"\n❌ 阈值过滤失败")
        return False


def test_6_workflow_integration():
    """测试 6: 工作流集成测试"""
    print_section("测试 6: 工作流集成测试")

    # 步骤 1: 使用 MCP 搜索文献
    print("步骤 1: 使用 MCP 搜索文献...")
    client = ZoteroMCPClient()
    search_result = client.search_library(query="U-Mo fuel", limit=3)

    if "data" not in search_result:
        print("❌ 搜索失败")
        return False

    papers = search_result["data"].get("results", [])
    print(f"   ✅ 找到 {len(papers)} 篇文献")

    # 步骤 2: 知识提取
    print("\n步骤 2: 执行知识提取...")
    extractor = KnowledgeExtractorFixed()
    extract_result = extractor.extract_from_papers(
        papers=papers,
        extract_numerical=True,
        extract_relations=True,
        confidence_threshold=0.6
    )

    if extract_result.get("status") != "success":
        print("❌ 提取失败")
        return False

    stats = extract_result.get("stats", {})
    print(f"   ✅ 提取成功")
    print(f"      总文献: {stats.get('total_papers', 0)}")
    print(f"      提取材料: {stats.get('total_materials', 0)}")
    print(f"      提取属性: {stats.get('total_properties', 0)}")
    print(f"      提取数值: {stats.get('extracted_values', 0)}")
    print(f"      提取关系: {stats.get('extracted_relations', 0)}")
    print(f"      平均置信度: {stats.get('avg_confidence', 0)}")

    print(f"\n✅ 工作流集成测试成功！")
    return True


def run_all_tests():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("  knowledge-extract-fixed 迁移测试套件")
    print("=" * 60)

    tests = [
        ("基本知识提取", test_1_basic_extraction),
        ("数值属性提取", test_2_numerical_extraction),
        ("关系提取", test_3_relation_extraction),
        ("完整提取", test_4_full_extraction),
        ("置信度阈值过滤", test_5_confidence_threshold),
        ("工作流集成测试", test_6_workflow_integration),
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
            import traceback
            traceback.print_exc()
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
