import { ReactNode } from "react";

import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

class TableComponent extends StreamlitComponentBase {
  args = this.props.args;
  name = this.args["name"];
  public render = (): ReactNode => {
    return <pre>{JSON.stringify(this.props, null, 2)}</pre>;
  };
}

const Component = withStreamlitConnection(TableComponent);
export default Component;
