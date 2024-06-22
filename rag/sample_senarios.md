A user, likely a developer or operations team member, who has access to these logs but doesn't know exactly what happened, might ask a high-level question like:

"We've been receiving complaints from customers in the AMER region about unfulfilled orders for PROD-X. Can you help me understand if there are any inventory or fulfillment issues based on yesterday's logs?"

This question reflects the issue they would have faced:

1. Customers in the AMER region are complaining about unfulfilled orders.
2. The problem seems to be specific to PROD-X.
3. They're not sure if it's an inventory problem or a fulfillment problem.
4. They've narrowed it down to yesterday's activities but don't know the exact cause.

This high-level question allows them to start investigating the issue without making assumptions about the root cause. It also reflects that they have access to the logs but haven't yet identified the specific problem amidst all the noise in the log data.


## prompt

Prompt:

"You are an AI assistant designed to analyze system logs and help diagnose issues in a complex distributed system. Given the following information:

1. A user question or reported issue: [INSERT USER QUESTION HERE]
2. A set of system logs: [INSERT LOGS HERE]

Please perform the following tasks:

1. Analyze the logs to identify any events or patterns relevant to the reported issue.
2. Trace the sequence of actions and events that might have led to the problem.
3. Identify any anomalies, errors, or unexpected behaviors in the logs that could be related to the issue.
4. Summarize your findings, focusing on the most likely root cause of the problem.
5. Provide a step-by-step explanation of what appears to have happened, based on the log evidence.
6. Suggest actionable steps to reproduce the issue, if possible.
7. Recommend potential solutions or areas for further investigation.

In your analysis, pay attention to:
- Timing and sequence of events
- Interactions between different services or components
- Any error messages or warnings
- Unusual patterns or deviations from expected behavior

Please present your findings in a clear, concise manner, suitable for a technical audience. If you make any assumptions or if there are areas where more information would be helpful, please state these clearly."

This prompt is designed to:
1. Be adaptable to different types of user questions and log formats.
2. Guide the LLM to perform the key tasks outlined in the PRD, including tracing user actions, understanding the issue, summarizing the root cause, and providing actionable steps.
3. Encourage a systematic analysis of the logs, looking for patterns and anomalies.
4. Result in a response that is helpful for developers and aligns with the goals of the proposed feature.

You can use this prompt by replacing [INSERT USER QUESTION HERE] with the actual user question (like "We've been receiving complaints from customers in the AMER region about unfulfilled orders for PROD-X.") and [INSERT LOGS HERE] with the relevant log data.