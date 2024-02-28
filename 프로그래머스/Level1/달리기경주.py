def solution(players, callings):
    p_idx_dict = {player: i for i, player in enumerate(players)}
    idx_p_dict = {i: player for i, player in enumerate(players)}
    
    for call in callings :
        cur_idx = p_idx_dict[call]  # 현재 선수의 위치
        pre_idx = cur_idx-1         # 현재 선수보다 앞에 있는 선수 위치
        cur_player = call
        pre_player = idx_p_dict[pre_idx]
        
        p_idx_dict[cur_player] = pre_idx
        p_idx_dict[pre_player] = cur_idx
        idx_p_dict[cur_idx] = pre_player
        idx_p_dict[pre_idx] = cur_player
    
    return list(idx_p_dict.values())