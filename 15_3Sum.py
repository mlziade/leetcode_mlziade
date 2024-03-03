## Time Limit Exceed

## Utilizei um hashtable com todos os nums da lista (valor como key e value é um array com todos as pos onde a key aparece)
## depois utilizo um loop duplo pra verificar se em cada tupla possivel existe um key cujo valor sem a (soma da dupla * -1)
## no terceiro loop só verifico se i != k != j e já adicionei esse triplet no vetor response (o sorted é utilizado pra fazer a verificação se já existe no vetor response)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = defaultdict(list)
        response = []
        size_arr = len(nums)
        for i in range(size_arr):
            numbers[nums[i]] += [i]

        for i in range(size_arr):
            for j in range(i+1, size_arr):
                tuple_sum = nums[i] + nums[j]
                missing_nums = numbers[tuple_sum * -1]
                for k in missing_nums:
                    if k not in [i,j]:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in response:
                            response.append(triplet)
        print(numbers)
        print(response)
        return response

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums_of_tuples = defaultdict(list)
        response = []
        size_arr = len(nums)
        for i in range(size_arr):
            for j in range(i+1, size_arr):
                sums_of_tuples[nums[i] + nums[j]] += [[i,j]]
        
        for i in range(size_arr):
            missing = sums_of_tuples[nums[i] * -1]
            print(missing)
            for k in missing:
                if i not in [k[0], k[1]]:
                    triplet = sorted([nums[k[0]], nums[k[1]], nums[i]])
                    if triplet not in response:
                        response.append(triplet)
        return response