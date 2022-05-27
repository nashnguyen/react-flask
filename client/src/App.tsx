import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Provider } from 'urql';

import { Layout } from './features/shared';
import client from './ultis/urql-client';

const App = () => {
  return (
    <Provider value={client}>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route
              path='/'
              element={<span className='text-blue-500'>Home</span>}
            ></Route>
            <Route
              path='/test'
              element={<span className='text-red-500'>Test Page</span>}
            ></Route>
          </Routes>
        </Layout>
      </BrowserRouter>
    </Provider>
  );
};

export default App;
