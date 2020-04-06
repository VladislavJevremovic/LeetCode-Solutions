// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<>();

            Queue<Node> queue = new LinkedList<>();
            queue.add(root);

            while (queue.peek() != null) {
                List<Integer> list = new ArrayList<>();
                Queue<Node> queue2 = new LinkedList<>();

                while (queue.peek() != null) {
                    Node node = queue.poll();

                    list.add(node.val);

                    for (Node nodeChild : node.children) {
                        queue2.add(nodeChild);
                    }
                }

                queue = queue2;
                result.add(list);
            }

            return result;
    }
}
