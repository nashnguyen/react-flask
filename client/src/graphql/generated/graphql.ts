import gql from 'graphql-tag';
import * as Urql from 'urql';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
};

export type Query = {
  __typename?: 'Query';
  salaries?: Maybe<Array<Maybe<Salary>>>;
};

export type Salary = {
  __typename?: 'Salary';
  id: Scalars['ID'];
  player: Scalars['String'];
  salary?: Maybe<Scalars['Int']>;
  season: Scalars['String'];
};

export type SalariesQueryVariables = Exact<{ [key: string]: never; }>;


export type SalariesQuery = { __typename?: 'Query', salaries?: Array<{ __typename?: 'Salary', id: string, player: string, season: string, salary?: number | null } | null> | null };


export const SalariesDocument = gql`
    query salaries {
  salaries {
    id
    player
    season
    salary
  }
}
    `;

export function useSalariesQuery(options?: Omit<Urql.UseQueryArgs<SalariesQueryVariables>, 'query'>) {
  return Urql.useQuery<SalariesQuery>({ query: SalariesDocument, ...options });
};