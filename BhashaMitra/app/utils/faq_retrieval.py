def retrieve_faq_answer(query, context):
    if "RTI" in query:
        return "RTI stands for Right to Information. It allows citizens to request information from government bodies."
    elif "subsidy" in query:
        return "A subsidy is financial help provided by the government to reduce the cost of goods or services."
    elif "clause" in query.lower():
        return "Clause 4 relates to the eligibility criteria for scheme participation."
    else:
        return "This section explains general rules or guidelines in the document."