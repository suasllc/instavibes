import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/index";
import Feed from "./components/Feed/index";
import Suggestions from "./components/Suggestions/index";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import User from "./components/User";
import UsersList from "./components/UserLists";
import ProfilePage from "./components/ProfilePage";
import NewPostTab from "./components/NewPostTab";
import HashtagPage from "./components/HashtagPage";
import ExplorePage from "./components/ExplorePage";
import { restoreUser } from "./store/session";
import Footer from "./components/footer/Footer";
import MessagePage from "./components/MessagePage";
import SinglePostPage from "./components/SinglePostPage";
import { StoryTopBox, StoriesFullPage } from "./components/Story";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    (async () => {
      await dispatch(restoreUser());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <div className="homepage">
        <NavBar />
        {user &&
          <NewPostTab />
        }
        <Switch>
          <Route path="/login" exact={true}>
            <LoginForm />
            <Footer />
          </Route>
          <Route path="/sign-up" exact={true}>
            <SignUpForm />
            <Footer />
          </Route>
          <ProtectedRoute path="/users" exact={true}>
            <UsersList />
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true}>
            <User />
          </ProtectedRoute>
          <ProtectedRoute path="/messages/:userId(\d*)" >
            <MessagePage />
          </ProtectedRoute>
          <ProtectedRoute path="/explore" exact={true}>
            <ExplorePage />
          </ProtectedRoute>
          <ProtectedRoute path="/p/:id" exact={true}>
            <SinglePostPage />
          </ProtectedRoute>
          <ProtectedRoute path="/" exact={true}>
            <div className="main_body">
              <div className="body_container">
                <div>
                  <StoryTopBox />
                  <Feed user={user} />
                </div>
                <Suggestions />
              </div>
            </div>
          </ProtectedRoute>
          <ProtectedRoute path="/explore/tags/:hashtag">
            <HashtagPage />
          </ProtectedRoute>
          <ProtectedRoute exact path="/:username">
            <ProfilePage tagged={false} />
            <Footer />
          </ProtectedRoute>
          <ProtectedRoute path="/:username/tagged">
            <ProfilePage tagged={true} />
            <Footer />
          </ProtectedRoute>
          <ProtectedRoute path="/:username/liked">
            <ProfilePage liked={true} />
            <Footer />
          </ProtectedRoute>
          <ProtectedRoute path="/:username/saved">
            <ProfilePage saved={true} />
            <Footer />
          </ProtectedRoute>
          <ProtectedRoute path="/stories/:username">
            <StoriesFullPage />
          </ProtectedRoute>
        </Switch>

      </div>
    </BrowserRouter>
  );
}

export default App;
