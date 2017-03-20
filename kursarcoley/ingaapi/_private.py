from inga import models as inga
import math

def build_unique_value(raw_data):
    unique_value = []

    for datum in raw_data:
        unique_value.append({
            "pc_id": datum.PC_ID,
            "rt_min": datum.RT - 0.20,
            "rt": datum.RT,
            "rt_max": datum.RT + 0.20,
            "mz_min": datum.MZ - 0.05,
            "mz": datum.MZ,
            "mz_max": datum.MZ + 0.05,
        })

    return unique_value


def build_multiple_value(unique_value):
    multiple_value = []

    for index, value_a in unique_value:
        for value_b in unique_value:
            if (value_a["pc_id"] == index
                    and value_b["pc_id"] > index
                    and value_b["rt_min"] <= value_a["rt"]
                    and value_b["rt_max"] >= value_a["rt"]):
                multiple_value.append({
                    "pc_id_a": value_a["pc_id"],
                    "pc_id_b": value_b["pc_id"],
                    "rt_min_destination": value_b["rt_min"],
                    "rt_origin": value_a["rt"],
                    "rt_max_destination": value_b["rt_max"]
                })

    return multiple_value


def build_multiple_value_mz(unique_value):
    multiple_value_mz = []

    for index, value_a in unique_value:
        for value_b in unique_value:
            if (value_a["pc_id"] == index
                    and value_b["pc_id"] > index
                    and value_b["mz_min"] <= value_a["mz"]
                    and value_b["mz_max"] >= value_a["mz"]):
                multiple_value_mz.append({
                    "pc_id_a": value_a["pc_id"],
                    "pc_id_b": value_b["pc_id"],
                    "mz_min_destination": value_b["mz_min"],
                    "mz_origin": value_a["mz"],
                    "mz_max_destination": value_b["mz_max"]
                })

    return multiple_value_mz


def build_multiple(multiple_value):
    multiple = []

    for value in multiple_value:
        if (round(abs(value["rt_origin"] - value["rt_min_destination"]), 2) <= 0.2
                and round(abs(value["rt_max_destination"] - value["rt_origin"]), 2) <= 0.2
                and value["pc_id_a"] != value["pc_id_b"]):
            multiple.append({
                "pc_id_a": value["pc_id_a"],
                "pc_id_b": value["pc_id_b"]
            })

    return multiple


def build_final_multiple(multiple_value_mz, multiple):
    final_multiple = []

    for mult in multiple:
        for mult_mz in multiple_value_mz:
            if (mult["pc_id_a"] == mult_mz["pc_id_a"]
                    and mult["pc_id_b"] == mult_mz["pc_id_b"]
                    and round(abs(mult_mz["mz_origin"] - mult_mz["mz_min_destination"]), 2) <= 0.05
                    and round(abs(mult_mz["mz_max_destination"] - mult_mz["mz_origin"]), 2) <= 0.05):
                final_multiple.append({
                    "id_origin": mult["pc_id_a"],
                    "id_destination": mult["pc_id_b"]
                })

    return final_multiple


def build_total_temp_div(raw_data):
    temp = {}
    total_temp_div = []

    for datum in raw_data:
        if datum.PC_ID in temp:
            temp[datum.PC_ID]["total"] += datum.TIC
            temp[datum.PC_ID]["count"] += 1
        else:
            temp[datum.PC_ID] = {
                "total": datum.TIC,
                "count": 1
            }

    for PC_ID in temp:
        total_temp_div.append({
            "pc_id": PC_ID,
            "total": temp[PC_ID]["total"],
            "average": temp[PC_ID]["total"] / temp[PC_ID]["count"]
        })

    return total_temp_div


def build_pc_id(total_temp_div, raw_data):
    temp = {}
    pc_id = []

    for datum in raw_data:
        for value in total_temp_div:
            if value["pc_id"] == datum.PC_ID:
                if value["pc_id"] in temp:
                    temp["pc_id"] = {
                        "sum": datum.TIC / value["total"]
                        "mz_rt": str(datum.MZ) + "_" + str(datum.RT)
                        "average": value["average"],
                        "total": value["total"]
                    }
                else:
                    temp["pc_id"]["sum"] += datum.TIC / value["total"]

    for value in temp:
        pc_id.append({
            "pc_id": value,
            "mz_rt": temp[value]["mz_rt"],
            "percent_tic": temp[value]["sum"] / temp[value]["total"]
            "average_tic": temp[value]["average"]
        })

    return pc_id


def build_identity_1(final_multiple, raw_data):
    
