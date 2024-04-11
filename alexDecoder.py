def decoder(password):
    ans2 = []
    for i in range(0, len(password)):
        ans2.append(int(password[i]) - 3)
        if ans2[i] <= -1:
            ans2[i] += 10
    ans2 = ''.join(map(str, ans2))
    return ans2