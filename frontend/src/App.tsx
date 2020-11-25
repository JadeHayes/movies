import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import styled from 'styled-components';
import Col from 'antd/lib/grid/col';
import Row from 'antd/lib/grid/row';
import 'antd/dist/antd.css';
import { LikeOutlined, DislikeOutlined, SearchOutlined } from '@ant-design/icons';
import Input from 'antd/lib/input';

interface MovieObject {
  title: string
  image: string
  id: string
}

const StyledResContainer = styled.div`
    cursor: pointer;
`;

const StlyedMovieImg = styled.img`
  height: 200px;
  width: 150px;
`;

const StlyedInput = styled(Input)`
  width: 300px;
`;


const StyledCol = styled(Col)`
  height: 300px;
  width: 300px;
`;

const App = () => {
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:5000/").then((res: AxiosResponse) => {
      setMovies(res.data)
    })
  }, [])

  return (
    <>
      <StlyedInput size="large" placeholder="Monty Python" suffix={
        <SearchOutlined />
      }/>
      <Row gutter={[16, 16]}>
        {movies.map((movie: MovieObject) => <StyledCol span={6}>
          <h4>{movie.title}</h4>
          <StlyedMovieImg src={movie.image} />
          <StyledResContainer>
            <LikeOutlined label='like' />
            <DislikeOutlined label='dislike' />
          </StyledResContainer>
        </StyledCol>
        )}
      </Row>
    </>
  );
}

export default App;
