// Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

const TreeNode = function(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
const kthSmallest = (root, k) => {
  // Build array from contents of BST using in order traversal
  const traversal = [];
  // Helper function to perform in order traversal
  // will build a sorted array with contents of bst in traversal
  const traverse = (node) => {
    if (node.left) {
      traverse(node.left);
    }
    traversal.push(node.val);
    if (node.right) {
      traverse(node.right);
    }
  }
  traverse(root);
  return traversal[k-1];
}

const test = () => {
  let root = new TreeNode(3);
  let branch1 = new TreeNode(1);
  root.left = branch1;
  let leaf1 = new TreeNode(2);
  branch1.right = leaf1;
  let branch2 = new TreeNode(4);
  root.right = branch2;
  console.log(kthSmallest(root, 1) == 1);

}
test();