import type { Comment } from "../../../types/comment";

export class JSONToTree {
    #json: Comment[] = new Array<Comment>();

    constructor(json: object[]) {
        this.#json = this.convert_to_tree_given_path(json);
    }

    private convert_to_tree_given_path(data: any): any {
        const tree: Comment[] = [];

        data.forEach((node: Comment) => {
            const path_segments = node.path.split(".");
            let current_node: Comment[] = tree;

            path_segments.forEach((segment, index) => {
                const existing_node = current_node.find((n) => n.path === segment);

                if (existing_node) {
                    current_node = existing_node.child;
                } else {
                    let new_node: any = { path: segment, child: [] };

                    if (index === path_segments.length - 1) {
                        // Copy values
                        const { child, path, ...rest } = node;
                        Object.assign(new_node, rest);
                    }

                    current_node.push(new_node);
                    current_node = new_node.child;
                }
            });
        });
        return tree;
    }

    public to_tree() {
        return this.#json;
    }
}
