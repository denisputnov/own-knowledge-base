import { useState } from 'react'
import classes from './App.module.css'
import ReactMarkdown from 'react-markdown'

function App() {
  const [input, setInput] = useState();
  console.log(input);
  return (
    <div className={classes.App}>
      <textarea
        autoFocus
        className={classes.Textarea}
        value={input}
        onChange={e => setInput(e.target.value)}
      />
      <ReactMarkdown children={input} className={classes.Markdown} />
    </div>
  );
}

export default App;
