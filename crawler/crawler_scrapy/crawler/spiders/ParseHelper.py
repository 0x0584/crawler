# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ParseHelper.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 18:20:53 by archid-           #+#    #+#              #
#    Updated: 2020/02/11 21:59:57 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# contains css selectors and regular expressions used in parsing
class ParseHelper:
    parseTitle = 'div.story-body h1.story-body__h1::text'
    parseSummary = 'div.story-body p.story-body__introduction::text'
    parseBody = 'div.story-body__inner p::text'
    parseArticles = 'div.gel-layout__item .gs-c-promo-body a.gs-o-faux-block-link__overlay-link::attr(href)'
    parseDatetime = 'div.date::attr(data-datetime)'
    parseAuthor = 'div.byline span.byline__name::text'
    parseTags = 'ul.tags-list li a::text'
    reArticles = '^/\S+'
    reLinks = r'https?://\S+'
