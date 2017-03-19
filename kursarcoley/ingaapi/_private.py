from inga import models as inga
import math

def build_baseline(raw_data):
    multiple_value_rt = []
    multiple_value_mz = []
    final = []

    for idx, a in enumerate(raw_data):
        for b in raw_data:
            if b.id > idx and
               a.id == idx and
               b.rt - 0.2 <= a.rt and
               b.rt + 0.2 >= a.rt:
                multiple_value_rt.append((a.id, b.id, b.rt - 0.2, a.rt, b.rt + 0.2))

            if b.id > idx and 
               a.id == idx and
               b.mz - 0.5 <= a.mz and
               b.mz + 0.5 >= a.mz:
                multiple_value_mz.append((a.id, b.id, b.mz - 0.5, a.mz, b.mz + 0.5))



    for value in multiple_value_rt:
        if value[0] != value[1]:
            if round(abs(value[3] - value[2]), 2) <= 0.2 and
               round(abs(value[4] - value[3]), 2) <= 0.2:
                final.append((value[0], value[1]))

            if round(abs(value[3] - value[2]), 2) <= 0.05 and
               round(abs(value[4] - value[3]), 2) <= 0.05:
                final.append((value[0], value[1]))


def build_pc_id(raw_data):
    initial, pc_id = {}
    
    for datum in raw_data:
        if datum.pc_id in initial:
            initial[datum.pc_id]["count"] += 1
            initial[datum.pc_id]["total"] += datum.tic
        else:
            initial[datum.pc_id] = {
                "count": 1,
                "total": datum.tic
            }
    
    for datum in raw_data:
        if datum.pc_id in initial:
            initial[datum.pc_id]["count"] += 1
            initial[datum.pc_id]["total"] += datum.tic
        else:
            initial[datum.pc_id] = {
                "count": 1,
                "total": datum.tic
            }
            