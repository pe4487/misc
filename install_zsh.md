# Install zsh on macOS



## 1.Install zsh

```
# install
brew install zsh

# change default shell
sudo sh -c "echo $(which zsh) >> /etc/shells" 
chsh -s $(which zsh)
```

## 2.Change iTerm theme

https://github.com/mbadolato/iTerm2-Color-Schemes

## 3.Powerline fonts

### powerline fonts

https://github.com/powerline/fonts

### awesome powerline font 

https://github.com/gabrielelana/awesome-terminal-fonts/tree/patching-strategy/patched

### office code pro

https://github.com/nathco/Office-Code-Pro

## 4. Install oh-my-zsh and powerlevel9k

```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

```
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

Edit your `~/.zshrc` and set `ZSH_THEME="powerlevel9k/powerlevel9k"`.



## 5.Plugin

### Syntax Hightlighting

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### Auto suggestion

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

Edit `~/.zshrc`  add `plugins=(zsh-autosuggestions zsh-syntax-highlighting)`

