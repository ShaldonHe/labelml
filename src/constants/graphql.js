import gql from 'graphql-tag'


export const SAVE_OBJ_DETECT_IMAGE = gql`
mutation SaveObjDetectImage($id: String!, $project: String!, 
                            $bboxes: [BoundingBoxInput]) {
    saveObjDetectImage(id: $id, project: $project, 
                       bboxes: $bboxes) {
        id
    }
}
`

export const NEXT_OBJ_DETECT_IMG_QUERY = gql`
query NextObjDetectImage($project:String!) {
    nextObjDetectImage(project: $project) {
        id
        project
        src
        bboxes {
          	id
            label
            score
            xmin
            ymin
            xmax
            ymax
        }
    }
  }
`;

export const OBJ_DETECT_IMG_QUERY = gql`
query ObjDetectImageQuery($id:String!, $project:String!) {
    objDetectImage(id: $id, project: $project) {
        id
        project
        src
        bboxes {
          	id
            label
            score
            xmin
            ymin
            xmax
            ymax
        }
    }
  }
`;

export const OBJ_DETECT_LABEL_OPT_QUERY = gql`
query ObjDetectLabelOptQuery($project:String!) {
    objDetectLabelOpts(project: $project) {
        labels {
          	value
            color
        }
    }
}
`;