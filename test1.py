    id1 = str(bangumi_result["b_id"])
    b_cn_name = bangumi_result["b_cn_name"]
    prev_id = ""

    print(f"{b_cn_name}的ID为{b_id}")
    bangumi_prev_result = api.bangumi_previous(b_id, b_cn_name)
    id2 = bangumi_prev_result[0]

    while id1 != id2:
        id1 = id2

        bangumi_prev_result = api.bangumi_previous(b_id, b_cn_name)
        id2 = bangumi_prev_result[0]


    print("ok")