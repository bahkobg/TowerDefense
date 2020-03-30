import pygame

menu_imgs = [pygame.image.load('assets/menus/upgrade/' + str(x) + '.png') for x in range(6)]


class MenuButton:
    def __init__(self, x, y, width, height, img, button_id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.button_id = button_id
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return self.button_id
        else:
            return False

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))


class UpgradeButton(MenuButton):
    def __init__(self, x, y, img, price, button_id):
        super().__init__(x, y, 96, 96, img, button_id)
        self.x = x
        self.y = y
        self.img = img
        self.price = price
        self.text = pygame.font.Font(None, 26)
        self.img_price = pygame.transform.scale(pygame.image.load('assets/menus/upgrade/6.png'), (48, 28))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        surface.blit(pygame.transform.scale(self.img_price, (48, 28)), (self.x + 52, self.y + 74))
        surface.blit(self.text.render(str(self.price), True, (255, 255, 255)), (self.x + 58, self.y + 82))


class UpgradeMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 328
        self.height = 150
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.button_quit = MenuButton(self.x + 304, self.y - 10, 32, 32, menu_imgs[1], 'QUIT')
        self.shape_upgrade = MenuButton(self.x + 100, self.y - 20, 128, 53, menu_imgs[2], False)
        self.button_upgrade_damage = UpgradeButton(self.x + 10, self.y + 35, menu_imgs[5], 12, 'DAMAGE')
        self.button_upgrade_range = UpgradeButton(self.x + 116, self.y + 35, menu_imgs[3], 22, 'RANGE')
        self.button_upgrade_defense = UpgradeButton(self.x + 222, self.y + 35, menu_imgs[4], 32, 'DEFENSE')
        self.buttons = [self.button_upgrade_defense, self.button_upgrade_range, self.button_quit, self.button_upgrade_damage]
        self.clicked = False

    def draw(self, surface):
        if self.clicked:
            surface.blit(pygame.transform.scale(menu_imgs[0], (self.width, self.height)), (self.x, self.y))
            self.button_quit.draw(surface)
            self.shape_upgrade.draw(surface)
            self.button_upgrade_damage.draw(surface)
            self.button_upgrade_range.draw(surface)
            self.button_upgrade_defense.draw(surface)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            for b in self.buttons:
                return b.click(pos)
        else:
            return False
