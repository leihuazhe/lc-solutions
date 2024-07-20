package leetcode;

import java.util.*;

public class FindNetworkEndpoint {

    public int findNetworkEndpoint(int startNodeId, List<Integer> fromIds, List<Integer> toIds) {
        // build adjacency list
        Map<Integer, List<Integer>> adjMap = new HashMap<>();

        for (int i = 0; i < fromIds.size(); i++) {
            int finalI = i;
            adjMap.compute(fromIds.get(i), (key, value) -> {
                if (value == null) {
                    value = new ArrayList<>();
                }
                value.add(toIds.get(finalI));
                return value;
            });
        }
        //2.使用 dfs start node  to end node, prevent repeat visit
        Set<Integer> visited = new HashSet<>();
        return dfs(startNodeId, adjMap, visited);
    }

    public int dfs(int startNodeId, Map<Integer, List<Integer>> adjMap, Set<Integer> visited) {
        visited.add(startNodeId);
        int endPoint = startNodeId;
        if (adjMap.containsKey(startNodeId)) {
            for (Integer adj : adjMap.get(startNodeId)) {
                if (!visited.contains(adj)) {
                    endPoint = dfs(adj, adjMap, visited);
                }
            }
        }
        return endPoint;
    }

    public static void main(String[] args) {
        FindNetworkEndpoint endpoint = new FindNetworkEndpoint();
        System.out.println(endpoint.findNetworkEndpoint(7, Arrays.asList(7, 3, 4, 6, 9, 2), Arrays.asList(3, 4, 6, 9, 5, 6)));
        System.out.println(endpoint.findNetworkEndpoint(6, Arrays.asList(4, 9, 6, 1), Arrays.asList(9, 5, 1, 4)));
    }
}
