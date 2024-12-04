import { ReactNode } from "react";

import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

class CounterComponent extends StreamlitComponentBase {
  args = this.props.args;
  name = this.args["name"];

  state = { counter: 0 };

  public render = (): ReactNode => {
    return (
      <div style={{ padding: "12px" }}>
        <h1>Counter is: {this.state.counter}</h1>
        <button
          onClick={() => this.setState({ counter: this.state.counter + 1 })}
        >
          Increase
        </button>
      </div>
    );
  };
}

const Component = withStreamlitConnection(CounterComponent);
export default Component;
