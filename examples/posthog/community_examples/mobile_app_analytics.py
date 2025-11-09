#!/usr/bin/env python3
"""
Mobile App Analytics with PostHog + GenOps

This example demonstrates mobile app analytics tracking with PostHog and GenOps
governance. It covers app lifecycle events, user engagement, feature usage,
performance monitoring, and in-app purchase tracking with cost intelligence.

Use Case:
    - iOS/Android mobile app user behavior tracking
    - App lifecycle and session management
    - Feature adoption and engagement analytics
    - Performance and crash reporting with governance
    - In-app purchase and subscription tracking

Usage:
    python community_examples/mobile_app_analytics.py

Prerequisites:
    pip install genops[posthog]
    export POSTHOG_API_KEY="phc_your_project_api_key"
    export GENOPS_TEAM="mobile-team"
    export GENOPS_PROJECT="mobile-app-analytics"

Expected Output:
    Complete mobile app session tracking with user engagement metrics,
    feature usage analytics, and performance monitoring with governance.

Learning Objectives:
    - Mobile app event taxonomy and lifecycle tracking
    - User engagement and retention analytics patterns
    - Performance monitoring with cost-aware telemetry
    - In-app purchase and subscription revenue tracking

Author: GenOps AI Community
License: Apache 2.0
"""

import time
import random
from datetime import datetime, timedelta
from typing import Dict, Any, List
from decimal import Decimal

def main():
    """Demonstrate comprehensive mobile app analytics with PostHog + GenOps."""
    print("📱 Mobile App Analytics with PostHog + GenOps")
    print("=" * 50)
    print()
    
    # Import and setup GenOps PostHog adapter
    try:
        from genops.providers.posthog import GenOpsPostHogAdapter
        print("✅ GenOps PostHog integration loaded")
    except ImportError as e:
        print(f"❌ Failed to import GenOps PostHog: {e}")
        print("💡 Fix: pip install genops[posthog]")
        return False
    
    # Initialize mobile app analytics adapter
    print("\n🎯 Setting up Mobile App Analytics Configuration...")
    adapter = GenOpsPostHogAdapter(
        team="mobile-analytics",
        project="fitness-tracker-app",
        environment="production",
        customer_id="mobile_app_ios",
        cost_center="mobile_development",
        daily_budget_limit=75.0,  # Mobile apps typically have high event volumes
        governance_policy="advisory",  # Flexible for mobile event bursts
        tags={
            'app_platform': 'ios',
            'app_version': '3.2.1',
            'analytics_tier': 'standard',
            'crash_reporting': 'enabled',
            'performance_monitoring': 'enabled'
        }
    )
    
    print("✅ Mobile app adapter configured")
    print(f"   📱 Platform: iOS")
    print(f"   📊 Daily budget: ${adapter.daily_budget_limit}")
    print(f"   📈 App version: 3.2.1")
    print(f"   🔍 Performance monitoring: Enabled")
    
    # Mobile user segments for realistic simulation
    user_segments = [
        {
            'segment': 'new_user', 
            'session_length': (2, 8),  # minutes
            'feature_adoption': 0.3,
            'retention_day_1': 0.4
        },
        {
            'segment': 'active_user',
            'session_length': (5, 20), 
            'feature_adoption': 0.7,
            'retention_day_1': 0.8
        },
        {
            'segment': 'power_user',
            'session_length': (15, 45),
            'feature_adoption': 0.9,
            'retention_day_1': 0.95
        }
    ]
    
    # Simulate multiple mobile app sessions
    print("\n" + "="*50)
    print("📲 Simulating Mobile App User Sessions")
    print("="*50)
    
    total_sessions = 0
    total_events = 0
    total_revenue = 0.0
    feature_usage = {}
    
    for session_id in range(1, 6):  # 5 mobile app sessions
        segment = random.choice(user_segments)
        user_id = f"mobile_user_{session_id:03d}"
        device_info = generate_device_info()
        
        print(f"\n📱 Session #{session_id}: {segment['segment'].replace('_', ' ').title()}")
        print("-" * 40)
        print(f"   Device: {device_info['model']} ({device_info['os_version']})")
        
        with adapter.track_analytics_session(
            session_name=f"mobile_session_{session_id}",
            customer_id=user_id,
            cost_center="mobile_user_acquisition",
            user_segment=segment['segment'],
            device_model=device_info['model']
        ) as session:
            
            session_events = 0
            session_duration = random.randint(*segment['session_length'])
            
            # 1. App Launch and Initialization
            print("🚀 App Launch & Initialization")
            
            # App opened event
            result = adapter.capture_event_with_governance(
                event_name="app_opened",
                properties={
                    "app_version": "3.2.1",
                    "device_model": device_info['model'],
                    "os_version": device_info['os_version'],
                    "app_build": "3210",
                    "launch_time_ms": random.randint(800, 2500),
                    "cold_start": random.choice([True, False]),
                    "user_segment": segment['segment']
                },
                distinct_id=user_id,
                session_id=session.session_id
            )
            session_events += 1
            print(f"   ✅ App opened - Launch time: {result['properties'].get('launch_time_ms', 'N/A')}ms - Cost: ${result['cost']:.6f}")
            
            # Screen views (core app navigation)
            screens = ['dashboard', 'workout_list', 'profile', 'settings', 'stats']
            screens_visited = random.sample(screens, random.randint(2, len(screens)))\n            \n            for screen in screens_visited:\n                result = adapter.capture_event_with_governance(\n                    event_name=\"screen_viewed\",\n                    properties={\n                        \"screen_name\": screen,\n                        \"previous_screen\": screens_visited[screens_visited.index(screen)-1] if screens_visited.index(screen) > 0 else \"app_launch\",\n                        \"view_duration_seconds\": random.randint(5, 60),\n                        \"user_segment\": segment['segment']\n                    },\n                    distinct_id=user_id,\n                    is_identified=True,  # Screen views are identified events\n                    session_id=session.session_id\n                )\n                session_events += 1\n                print(f\"   📺 Screen '{screen}' viewed - Cost: ${result['cost']:.6f}\")\n            \n            # 2. Feature Usage and Engagement\n            print(\"\\n🎯 Feature Usage & Engagement\")\n            \n            # Core feature usage based on user segment\n            features = [\n                {'name': 'workout_start', 'adoption_rate': 0.8, 'revenue_potential': 0.0},\n                {'name': 'progress_tracking', 'adoption_rate': 0.6, 'revenue_potential': 0.0},\n                {'name': 'social_sharing', 'adoption_rate': 0.3, 'revenue_potential': 0.0},\n                {'name': 'premium_workout', 'adoption_rate': 0.1, 'revenue_potential': 9.99},\n                {'name': 'nutrition_planner', 'adoption_rate': 0.2, 'revenue_potential': 4.99}\n            ]\n            \n            for feature in features:\n                if random.random() < feature['adoption_rate'] * segment['feature_adoption']:\n                    feature_usage[feature['name']] = feature_usage.get(feature['name'], 0) + 1\n                    \n                    result = adapter.capture_event_with_governance(\n                        event_name=\"feature_used\",\n                        properties={\n                            \"feature_name\": feature['name'],\n                            \"usage_duration_seconds\": random.randint(30, 300),\n                            \"user_segment\": segment['segment'],\n                            \"feature_discovery\": random.choice(['onboarding', 'organic', 'notification', 'search'])\n                        },\n                        distinct_id=user_id,\n                        is_identified=True,\n                        session_id=session.session_id\n                    )\n                    session_events += 1\n                    print(f\"   🔧 Feature '{feature['name']}' used - Cost: ${result['cost']:.6f}\")\n                    \n                    # In-app purchase simulation for premium features\n                    if feature['revenue_potential'] > 0 and random.random() < 0.15:  # 15% purchase rate\n                        result = adapter.capture_event_with_governance(\n                            event_name=\"in_app_purchase\",\n                            properties={\n                                \"product_id\": f\"premium_{feature['name']}\",\n                                \"price\": feature['revenue_potential'],\n                                \"currency\": \"USD\",\n                                \"purchase_type\": \"one_time\",\n                                \"payment_method\": \"app_store\",\n                                \"user_segment\": segment['segment']\n                            },\n                            distinct_id=user_id,\n                            is_identified=True,\n                            session_id=session.session_id\n                        )\n                        session_events += 1\n                        total_revenue += feature['revenue_potential']\n                        print(f\"   💰 In-app purchase: ${feature['revenue_potential']} - Cost: ${result['cost']:.6f}\")\n            \n            # 3. Performance and Technical Events\n            print(\"\\n⚡ Performance & Technical Monitoring\")\n            \n            # Performance metrics\n            if random.random() < 0.7:  # 70% of sessions report performance\n                result = adapter.capture_event_with_governance(\n                    event_name=\"performance_metric\",\n                    properties={\n                        \"metric_type\": \"app_performance\",\n                        \"cpu_usage_percent\": random.uniform(10, 80),\n                        \"memory_usage_mb\": random.randint(150, 400),\n                        \"battery_drain_percent\": random.uniform(1, 5),\n                        \"network_requests\": random.randint(5, 25),\n                        \"user_segment\": segment['segment']\n                    },\n                    distinct_id=user_id,\n                    session_id=session.session_id\n                )\n                session_events += 1\n                print(f\"   📊 Performance metrics captured - Cost: ${result['cost']:.6f}\")\n            \n            # Error/crash reporting (low probability)\n            if random.random() < 0.05:  # 5% chance of error\n                error_types = ['network_timeout', 'ui_freeze', 'data_sync_failed', 'crash']\n                error_type = random.choice(error_types)\n                \n                result = adapter.capture_event_with_governance(\n                    event_name=\"app_error\",\n                    properties={\n                        \"error_type\": error_type,\n                        \"error_message\": f\"Mobile app {error_type} in session\",\n                        \"stack_trace_available\": random.choice([True, False]),\n                        \"user_segment\": segment['segment'],\n                        \"app_state\": random.choice(['foreground', 'background'])\n                    },\n                    distinct_id=user_id,\n                    is_identified=True,\n                    session_id=session.session_id\n                )\n                session_events += 1\n                print(f\"   ⚠️ App error '{error_type}' reported - Cost: ${result['cost']:.6f}\")\n            \n            # 4. Session End and Engagement\n            print(\"\\n👋 Session End & Engagement Summary\")\n            \n            # Session completed\n            result = adapter.capture_event_with_governance(\n                event_name=\"session_ended\",\n                properties={\n                    \"session_duration_minutes\": session_duration,\n                    \"screens_visited\": len(screens_visited),\n                    \"features_used\": len([f for f in features if f['name'] in feature_usage]),\n                    \"user_segment\": segment['segment'],\n                    \"session_quality\": \"high\" if session_duration > 10 else \"standard\"\n                },\n                distinct_id=user_id,\n                session_id=session.session_id\n            )\n            session_events += 1\n            print(f\"   ✅ Session ended - Duration: {session_duration}min - Cost: ${result['cost']:.6f}\")\n            \n            # App backgrounded\n            result = adapter.capture_event_with_governance(\n                event_name=\"app_backgrounded\",\n                properties={\n                    \"background_trigger\": random.choice(['home_button', 'notification', 'phone_call', 'app_switcher']),\n                    \"session_duration_minutes\": session_duration,\n                    \"user_segment\": segment['segment']\n                },\n                distinct_id=user_id,\n                session_id=session.session_id\n            )\n            session_events += 1\n            print(f\"   📱 App backgrounded - Cost: ${result['cost']:.6f}\")\n            \n            total_sessions += 1\n            total_events += session_events\n            \n            print(f\"\\n📊 Session Summary:\")\n            print(f\"   Events in session: {session_events}\")\n            print(f\"   Session duration: {session_duration} minutes\")\n            print(f\"   Screens visited: {len(screens_visited)}\")\n            print(f\"   User segment: {segment['segment'].replace('_', ' ').title()}\")\n            \n            # Realistic mobile timing\n            time.sleep(0.3)\n    \n    # Mobile app analytics summary\n    print(\"\\n\" + \"=\"*50)\n    print(\"📈 Mobile App Analytics Summary\")\n    print(\"=\"*50)\n    \n    cost_summary = adapter.get_cost_summary()\n    avg_session_length = sum([random.randint(*seg['session_length']) for seg in user_segments]) / len(user_segments)\n    \n    print(f\"📱 App Performance Metrics:\")\n    print(f\"   Total sessions tracked: {total_sessions}\")\n    print(f\"   Average session length: {avg_session_length:.1f} minutes\")\n    print(f\"   Total events captured: {total_events}\")\n    print(f\"   Events per session: {total_events/total_sessions:.1f}\")\n    print(f\"   In-app revenue tracked: ${total_revenue:.2f}\")\n    \n    print(f\"\\n🎯 Feature Adoption:\")\n    for feature, usage_count in feature_usage.items():\n        adoption_rate = (usage_count / total_sessions) * 100\n        print(f\"   {feature.replace('_', ' ').title()}: {usage_count}/{total_sessions} sessions ({adoption_rate:.1f}%)\")\n    \n    print(f\"\\n💰 Cost Intelligence:\")\n    print(f\"   Total analytics cost: ${cost_summary['daily_costs']:.6f}\")\n    print(f\"   Cost per session: ${cost_summary['daily_costs']/total_sessions:.6f}\")\n    print(f\"   Cost per event: ${cost_summary['daily_costs']/total_events:.6f}\")\n    print(f\"   Budget utilization: {cost_summary['daily_budget_utilization']:.1f}%\")\n    \n    print(f\"\\n🏛️ Mobile Governance:\")\n    print(f\"   Team: {cost_summary['team']}\")\n    print(f\"   Project: {cost_summary['project']}\")\n    print(f\"   Environment: {cost_summary['environment']}\")\n    print(f\"   Platform tracking: iOS/Android\")\n    print(f\"   Performance monitoring: Enabled\")\n    \n    # Mobile-specific insights\n    print(f\"\\n📊 Mobile App Insights:\")\n    if total_revenue > 0:\n        print(f\"   Revenue per analytics dollar: ${total_revenue / cost_summary['daily_costs']:.2f}\")\n        print(f\"   Analytics ROI: {(total_revenue / cost_summary['daily_costs']):.0f}x\")\n    print(f\"   Estimated monthly app analytics cost: ${cost_summary['daily_costs'] * 30:.2f}\")\n    print(f\"   Cost efficiency: ${cost_summary['daily_costs']/total_events * 1000:.3f} per 1K events\")\n    \n    print(f\"\\n✅ Mobile app analytics tracking completed successfully!\")\n    return True\n\ndef generate_device_info() -> Dict[str, str]:\n    \"\"\"Generate realistic mobile device information.\"\"\"\n    ios_devices = [\n        {\"model\": \"iPhone 14 Pro\", \"os_version\": \"iOS 16.4\"},\n        {\"model\": \"iPhone 13\", \"os_version\": \"iOS 16.3\"},\n        {\"model\": \"iPhone 12\", \"os_version\": \"iOS 16.2\"},\n        {\"model\": \"iPad Air\", \"os_version\": \"iOS 16.4\"}\n    ]\n    \n    android_devices = [\n        {\"model\": \"Samsung Galaxy S23\", \"os_version\": \"Android 13\"},\n        {\"model\": \"Google Pixel 7\", \"os_version\": \"Android 13\"},\n        {\"model\": \"OnePlus 11\", \"os_version\": \"Android 13\"},\n        {\"model\": \"Samsung Galaxy Tab\", \"os_version\": \"Android 12\"}\n    ]\n    \n    all_devices = ios_devices + android_devices\n    return random.choice(all_devices)\n\ndef get_mobile_analytics_recommendations() -> List[Dict[str, str]]:\n    \"\"\"Generate mobile app analytics optimization recommendations.\"\"\"\n    return [\n        {\n            \"category\": \"User Retention\",\n            \"recommendation\": \"Track user lifecycle stages for personalized onboarding\",\n            \"implementation\": \"Add user_lifecycle_stage to all events (new, activated, retained, churned)\",\n            \"expected_impact\": \"25-40% improvement in Day 1 retention\"\n        },\n        {\n            \"category\": \"Performance Optimization\",\n            \"recommendation\": \"Implement smart event batching for battery efficiency\",\n            \"implementation\": \"Batch non-critical events and send during charging/WiFi\",\n            \"expected_impact\": \"60-80% reduction in battery impact\"\n        },\n        {\n            \"category\": \"Cost Optimization\",\n            \"recommendation\": \"Use local analytics SDK with intelligent sync\",\n            \"implementation\": \"Cache events locally and sync based on connectivity/cost\",\n            \"expected_impact\": \"40-60% reduction in analytics costs\"\n        },\n        {\n            \"category\": \"Feature Discovery\",\n            \"recommendation\": \"Track feature discovery paths for UX optimization\",\n            \"implementation\": \"Add discovery_method to all feature_used events\",\n            \"expected_impact\": \"20-35% increase in feature adoption\"\n        }\n    ]\n\nif __name__ == \"__main__\":\n    try:\n        success = main()\n        \n        if success:\n            print(f\"\\n💡 Mobile Analytics Best Practices:\")\n            recommendations = get_mobile_analytics_recommendations()\n            for i, rec in enumerate(recommendations, 1):\n                print(f\"   {i}. {rec['category']}: {rec['recommendation']}\")\n                print(f\"      Implementation: {rec['implementation']}\")\n                print(f\"      Expected Impact: {rec['expected_impact']}\")\n                print()\n        \n        exit(0 if success else 1)\n        \n    except KeyboardInterrupt:\n        print(\"\\n\\n👋 Mobile analytics demonstration interrupted by user\")\n        exit(1)\n    except Exception as e:\n        print(f\"\\n💥 Error in mobile analytics example: {e}\")\n        print(\"🔧 Please check your PostHog configuration and try again\")\n        exit(1)"