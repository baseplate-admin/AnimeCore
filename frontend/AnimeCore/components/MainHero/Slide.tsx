import {
    ActionIcon,
    BackgroundImage,
    Badge,
    Box,
    Button,
    Container,
    createStyles,
    Grid,
    ScrollArea,
    Skeleton,
    Space,
    Text,
    Title,
    useMantineTheme,
} from '@mantine/core';
import { useMediaQuery } from '@mantine/hooks';
import React, { ElementRef, memo, useEffect, useRef, useState } from 'react';
import type { Swiper as SwiperType } from 'swiper';
import { useSwiper, useSwiperSlide } from 'swiper/react';

import Navbar from '@/components/common/Navbar';
import MainHeroProgress from '@/components/MainHero/Progress';

import AutoComplete from './AutoComplete';

const useStyles = createStyles((theme) => ({
    base: {
        minHeight: '100vh',

        [theme.fn.smallerThan('md')]: {
            minHeight: 600,
            maxHeight: 600, // Fix Me
        },
    },

    box: {
        display: 'flex',
    },

    root: {
        flexDirection: 'column',
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        height: 'inherit',
        color: 'black',

        boxShadow: `
            inset 0 4px calc(10vh + 1800px) rgb(7, 5, 25),
            inset 0 -40vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh calc(10vh + 140px) 2px rgba(7, 5, 25, 0.2)`,

        [theme.fn.smallerThan('md')]: {
            paddingBottom: theme.spacing.xs * 2,

            boxShadow: `
                inset 0px -30px 12px -2px rgba(7, 5, 25, 0.85),
                inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.8),
                inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)`,
        },
    },

    inner: {
        display: 'flex',

        [theme.fn.smallerThan('md')]: {
            flexDirection: 'column',
        },
    },

    image: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
    container: {
        marginTop: 'auto',
        marginLeft: 0,
        paddingLeft: theme.spacing.xl * 4,

        [theme.fn.smallerThan('md')]: {
            paddingLeft: theme.spacing.sm * 2,
            paddingRight: theme.spacing.sm * 2,
        },
    },
    content: {
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        marginRight: theme.spacing.xl * 3,

        [theme.fn.smallerThan('md')]: {
            marginRight: 0,
        },
    },

    title: {
        fontWeight: 900,
        lineHeight: 1.05,
        maxWidth: 500,
        fontSize: 48,
        display: 'flex',
        alignItems: 'center',

        [theme.fn.smallerThan('md')]: {
            maxWidth: '100%',
            fontSize: 34,
            lineHeight: 1.15,
        },
    },

    description: {
        color: theme.white,
        opacity: 0.75,
        maxWidth: 500,

        [theme.fn.smallerThan('md')]: {
            maxWidth: '100%',
        },
    },

    control: {
        paddingLeft: 50,
        paddingRight: 50,
        fontSize: 22,

        [theme.fn.smallerThan('md')]: {
            width: '100%',
        },
    },

    line: {
        color: theme.colors.yellow[6],
    },

    info: {
        ':after': {
            content: '" ▪ "',
        },
    },
    buttonContainer: {
        display: 'flex',
    },
    tagContainer: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
    infoContainer: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
    swiper__mainhero__pagination: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'row',

        [theme.fn.smallerThan('md')]: {
            width: 150,
        },
        [theme.fn.largerThan('md')]: {
            width: 270,
        },
    },
    swiper__bullet: {
        height: 22,
        lineHeight: 0.5,
        fontSize: 60,
        padding:
            '0px calc(var(--swiper-pagination-bullet-horizontal-gap) / 2) 0px',
        cursor: 'pointer',

        overflow: 'hidden',
    },
}));

interface IProps {
    animeTitle: string;
    animeSummary: string;
    animeEpisodeCount: number;
    animeStudio: string;
    animeAirTime: string;
    backgroundImage: string;
    backgroundBanner: string;
    tags: string[];
    swiper: Partial<SwiperType> | null;
}

const MainHeroSlide = memo(function MainHeroSlide(props: IProps) {
    const swiper = useSwiper();
    const swiperSlide = useSwiperSlide();

    const { classes } = useStyles();
    const theme = useMantineTheme();

    type ProgressHandle = ElementRef<typeof MainHeroProgress>;
    const progress = useRef<ProgressHandle>(null);

    const [heroBackgroundImage, setHeroBackgroundImage] = useState<string>('');

    const mobile = useMediaQuery('(min-width: 0px) and (max-width: 576px)');
    const tablet = useMediaQuery('(min-width: 577px) and (max-width: 768px)');
    const fullhd = useMediaQuery('(min-width: 769px) and (max-width: 992px)');

    // Hook to update slider progress

    useEffect(() => {
        if (mobile) {
            setHeroBackgroundImage(props.backgroundBanner);
        } else if (tablet) {
            setHeroBackgroundImage(props.backgroundImage);
        } else if (fullhd) {
            setHeroBackgroundImage(props.backgroundImage);
        } else {
            setHeroBackgroundImage(props.backgroundImage); // This is the normal one
        }
    }, [fullhd, tablet, mobile, props]);

    const [isLoading, setIsLoading] = useState<boolean>(true);

    useEffect(() => {
        setTimeout(() => {
            if (swiperSlide.isActive) {
                setIsLoading(false);
            } else {
                setIsLoading(true);
            }
        }, 400);
    }, [swiperSlide]);

    /** Start the swiper */

    progress?.current?.start();

    swiper.on('slideChange', () => {
        progress?.current?.start();
    });

    props.swiper?.on?.('slideChange', () => {
        if (props.swiper?.activeIndex !== 0) {
            progress.current?.reset();
        } else {
            progress?.current?.start();
        }
    });

    /** Events to handle scrollbox area */

    const mouseEntersScrollArea = (event: React.MouseEvent<HTMLDivElement>) => {
        if (event) {
            progress.current?.pause();

            props.swiper?.mousewheel?.disable();
        }
    };

    const mouseLeavesScrollArea = (event: React.MouseEvent<HTMLDivElement>) => {
        if (event) {
            progress.current?.start();

            props.swiper?.mousewheel?.enable();
        }
    };

    const touchEntersScrollArea = (event: React.TouchEvent<HTMLDivElement>) => {
        if (event) {
            progress?.current?.pause();

            props.swiper!.allowTouchMove = false;
        }
    };

    const touchLeavesScrollArea = (event: React.TouchEvent<HTMLDivElement>) => {
        if (event) {
            progress?.current?.start();

            props.swiper!.allowTouchMove = true;
        }
    };

    return (
        <Box className={`${classes.box} ${classes.base}`}>
            <BackgroundImage
                className={`${classes.root}`}
                src={
                    props?.swiper?.activeIndex === 0 ? heroBackgroundImage : ''
                }
                style={{
                    display: 'flex', // This is a weird hack to make the items align properly
                    backgroundColor: 'black', // Stupid Mantine
                }}
            >
                {swiperSlide.isActive ? (
                    <>
                        {mobile ? (
                            <>
                                <AutoComplete
                                    mr="xl"
                                    ml="xl"
                                    variant="filled"
                                    radius="md"
                                    size="md"
                                    onFocus={() => {
                                        progress?.current?.pause();
                                    }}
                                    onBlur={() => {
                                        progress?.current?.start();
                                    }}
                                    icon={
                                        <img
                                            src="/icons/search.svg"
                                            alt=""
                                            width={18}
                                            height={18}
                                        />
                                    }
                                    aria-label="Search Image"
                                    placeholder="Search for anything"
                                />
                            </>
                        ) : (
                            <>
                                <Navbar />
                            </>
                        )}
                        <Container size="lg" className={classes.container}>
                            <div className={classes.inner}>
                                <div className={classes.content}>
                                    <Title className={classes.title}>
                                        {isLoading ? (
                                            <>
                                                <Skeleton
                                                    height={20}
                                                    width={120}
                                                />
                                            </>
                                        ) : (
                                            <>
                                                <Text
                                                    component="span"
                                                    size="xl"
                                                    weight="bold"
                                                    color="yellow"
                                                    sx={(theme) => ({
                                                        [theme.fn.smallerThan(
                                                            'sm'
                                                        )]: {
                                                            fontSize:
                                                                theme.fontSizes
                                                                    .sm,
                                                        },
                                                    })}
                                                >
                                                    Featured
                                                </Text>
                                            </>
                                        )}

                                        <Space w="sm" />
                                        {isLoading ? (
                                            <>
                                                <Skeleton
                                                    height={20}
                                                    width={60}
                                                />
                                            </>
                                        ) : (
                                            <>
                                                <div
                                                    className={classes.line}
                                                    style={{
                                                        display: 'inline-block',
                                                        width: '60px',
                                                        borderTop: '4px solid',
                                                        borderRadius: 10,
                                                    }}
                                                />
                                            </>
                                        )}
                                    </Title>
                                    <Title order={1}>
                                        {isLoading ? (
                                            <>
                                                {mobile ? (
                                                    <>
                                                        <Skeleton
                                                            height={40}
                                                            mt="sm"
                                                        />
                                                    </>
                                                ) : (
                                                    <>
                                                        <Skeleton
                                                            mt="xl"
                                                            height={100}
                                                            mb="xl"
                                                        />
                                                    </>
                                                )}
                                            </>
                                        ) : (
                                            <>
                                                <ScrollArea
                                                    sx={(theme) => ({
                                                        height: 80,
                                                        [theme.fn.smallerThan(
                                                            'md'
                                                        )]: {
                                                            height: 40,
                                                        },
                                                    })}
                                                    onMouseEnter={
                                                        mouseEntersScrollArea
                                                    }
                                                    onMouseLeave={
                                                        mouseLeavesScrollArea
                                                    }
                                                    onTouchStart={
                                                        touchEntersScrollArea
                                                    }
                                                    onTouchEnd={
                                                        touchLeavesScrollArea
                                                    }
                                                    offsetScrollbars
                                                >
                                                    <Text
                                                        size="lg"
                                                        color="white"
                                                        inherit
                                                        sx={(theme) => ({
                                                            [theme.fn.smallerThan(
                                                                'sm'
                                                            )]: {
                                                                fontSize: 30, // Fix Me
                                                            },
                                                        })}
                                                    >
                                                        {props.animeTitle}
                                                    </Text>
                                                </ScrollArea>
                                            </>
                                        )}
                                    </Title>
                                    <Title className={classes.infoContainer}>
                                        {isLoading ? (
                                            <>
                                                <Skeleton
                                                    mt="lg"
                                                    width={270}
                                                    height={20}
                                                />
                                            </>
                                        ) : (
                                            <>
                                                <Text
                                                    className={classes.info}
                                                    component="span"
                                                    color="white"
                                                >
                                                    TV
                                                </Text>
                                                <Text
                                                    className={classes.info}
                                                    component="span"
                                                    color="white"
                                                >
                                                    {props.animeEpisodeCount}{' '}
                                                    eps
                                                </Text>
                                                <Text
                                                    className={classes.info}
                                                    component="span"
                                                    color="white"
                                                >
                                                    Completed
                                                </Text>
                                                <Text
                                                    className={classes.info}
                                                    component="span"
                                                    color="white"
                                                >
                                                    {props.animeAirTime}
                                                </Text>
                                                <Text
                                                    component="span"
                                                    color="white"
                                                >
                                                    {props.animeStudio}
                                                </Text>
                                                <Space h="md" />
                                            </>
                                        )}
                                    </Title>
                                    <>
                                        {isLoading ? (
                                            <>
                                                {mobile ? (
                                                    <>
                                                        <Skeleton
                                                            height={100}
                                                            width="80vw"
                                                            mt="sm"
                                                        />
                                                    </>
                                                ) : (
                                                    <>
                                                        {mobile ? (
                                                            <>
                                                                <Skeleton
                                                                    mt="sm"
                                                                    mb="md"
                                                                    height={100}
                                                                    width="80vw"
                                                                />
                                                            </>
                                                        ) : (
                                                            <>
                                                                <Skeleton
                                                                    mt="sm"
                                                                    mb="md"
                                                                    height={115}
                                                                    width="80vw"
                                                                />
                                                            </>
                                                        )}
                                                    </>
                                                )}
                                            </>
                                        ) : (
                                            <>
                                                <ScrollArea
                                                    style={{ height: 100 }}
                                                    onMouseEnter={
                                                        mouseEntersScrollArea
                                                    }
                                                    onMouseLeave={
                                                        mouseLeavesScrollArea
                                                    }
                                                    onTouchStart={
                                                        touchEntersScrollArea
                                                    }
                                                    onTouchEnd={
                                                        touchLeavesScrollArea
                                                    }
                                                    offsetScrollbars
                                                >
                                                    <Text
                                                        color="gray"
                                                        sx={() => ({
                                                            whiteSpace:
                                                                'pre-line',
                                                        })}
                                                    >
                                                        {props.animeSummary}
                                                    </Text>
                                                </ScrollArea>
                                            </>
                                        )}
                                    </>
                                    <div className={classes.tagContainer}>
                                        {isLoading ? (
                                            <>
                                                <Skeleton
                                                    height={25}
                                                    width="50vw"
                                                />
                                            </>
                                        ) : (
                                            <>
                                                <Space h="xl" />

                                                {props.tags.map(
                                                    (item, index) => {
                                                        return (
                                                            <Badge
                                                                key={index}
                                                                component="span"
                                                                size="lg"
                                                                radius="sm"
                                                                variant="filled"
                                                                mr="md"
                                                                style={{
                                                                    backgroundColor:
                                                                        theme
                                                                            .colors
                                                                            .blue[9],
                                                                }}
                                                            >
                                                                {item}
                                                            </Badge>
                                                        );
                                                    }
                                                )}
                                            </>
                                        )}
                                    </div>

                                    <div className={classes.buttonContainer}>
                                        {isLoading ? (
                                            <>
                                                {mobile ? (
                                                    <>
                                                        <Skeleton
                                                            mt="xl"
                                                            width={110}
                                                            height={60}
                                                        />
                                                    </>
                                                ) : (
                                                    <>
                                                        <Skeleton
                                                            mt="xl"
                                                            width={60}
                                                            height={60}
                                                        />
                                                    </>
                                                )}
                                            </>
                                        ) : (
                                            <>
                                                <Button
                                                    mt="xl"
                                                    color="yellow"
                                                    style={{
                                                        backgroundColor:
                                                            theme.colors
                                                                .yellow[9],
                                                    }}
                                                    sx={(theme) => ({
                                                        height: 60,

                                                        [theme.fn.largerThan(
                                                            'sm'
                                                        )]: {
                                                            width: 60,
                                                        },
                                                    })}
                                                    radius="lg"
                                                >
                                                    <img
                                                        alt=""
                                                        src="/icons/play.svg"
                                                        width={24}
                                                        height={24}
                                                    />
                                                    <Text
                                                        color="dark"
                                                        weight={700}
                                                    >
                                                        Watch
                                                    </Text>
                                                </Button>
                                            </>
                                        )}
                                        {isLoading ? (
                                            <>
                                                <Skeleton
                                                    ml="xl"
                                                    mt="xl"
                                                    height={60}
                                                    width={120}
                                                />
                                            </>
                                        ) : (
                                            <>
                                                <Button
                                                    ml="xl"
                                                    mt="xl"
                                                    color="yellow"
                                                    variant="outline"
                                                    style={{
                                                        borderWidth: 4,
                                                        borderColor:
                                                            theme.colors
                                                                .yellow[9],
                                                        height: 60,
                                                    }}
                                                    radius="lg"
                                                    rightIcon={
                                                        <img
                                                            alt=""
                                                            src="/icons/chevrons-right.svg"
                                                            width={24}
                                                            height={24}
                                                        />
                                                    }
                                                >
                                                    <Text
                                                        weight={700}
                                                        size="lg"
                                                        color="yellow"
                                                    >
                                                        Details
                                                    </Text>
                                                </Button>
                                            </>
                                        )}
                                    </div>
                                </div>
                            </div>
                        </Container>
                        <Title
                            sx={() => ({
                                backgroundColor: '',
                                display: 'flex',
                            })}
                        >
                            <Grid
                                grow
                                justify="space-between"
                                align="center"
                                sx={() => ({
                                    height: '100%',
                                    width: '100%',
                                })}
                            >
                                <Grid.Col
                                    span={3}
                                    sx={(theme) => ({
                                        [theme.fn.smallerThan('md')]: {
                                            display: 'none',
                                        },
                                    })}
                                />
                                <Grid.Col
                                    span={3}
                                    sx={() => ({
                                        display: 'flex',
                                        justifyContent: 'center',
                                        alignItems: 'center',
                                        height: '10vh',
                                        maxWidth: '100vw',
                                        flexDirection: 'row',
                                    })}
                                >
                                    {swiperSlide.isActive ? (
                                        <>
                                            <MainHeroProgress ref={progress} />
                                        </>
                                    ) : (
                                        <></>
                                    )}
                                    <div
                                        className={
                                            classes.swiper__mainhero__pagination
                                        }
                                    >
                                        {Array(swiper?.slides.length - 2)
                                            .fill(0)
                                            .map((__, index) => (
                                                <div
                                                    key={index}
                                                    className={
                                                        classes.swiper__bullet
                                                    }
                                                    style={{
                                                        color:
                                                            swiper?.realIndex ===
                                                            index
                                                                ? 'var(--swiper-pagination-bullet-inactive-color)'
                                                                : '',
                                                        opacity:
                                                            swiper?.realIndex ===
                                                            index
                                                                ? 1
                                                                : 'var(--swiper-pagination-bullet-inactive-opacity)',
                                                    }}
                                                    onClick={async () => {
                                                        swiper.slideTo(
                                                            index + 1
                                                        );
                                                    }}
                                                >
                                                    ·
                                                </div>
                                            ))}
                                    </div>
                                    <ActionIcon
                                        color="yellow"
                                        size="lg"
                                        ml="xl"
                                        radius="md"
                                        variant="filled"
                                        sx={(theme) => ({
                                            [theme.fn.smallerThan('md')]: {
                                                display: 'none',
                                            },
                                        })}
                                        onClick={async () => {
                                            swiper.slidePrev();
                                        }}
                                    >
                                        <img
                                            src="icons/chevron-left-black.svg"
                                            alt=""
                                        />
                                    </ActionIcon>
                                    <ActionIcon
                                        color="yellow"
                                        size="lg"
                                        radius="md"
                                        variant="filled"
                                        ml="xl"
                                        onClick={async () => {
                                            swiper.slideNext();
                                        }}
                                        sx={(theme) => ({
                                            [theme.fn.smallerThan('md')]: {
                                                display: 'none',
                                            },
                                        })}
                                    >
                                        <img
                                            src="icons/chevron-right-black.svg"
                                            alt=""
                                        />
                                    </ActionIcon>
                                </Grid.Col>
                                <Grid.Col
                                    span={3}
                                    sx={(theme) => ({
                                        display: 'flex',
                                        justifyContent: 'flex-end',

                                        [theme.fn.smallerThan('md')]: {
                                            display: 'none',
                                        },
                                    })}
                                >
                                    <img
                                        width={24}
                                        height={24}
                                        src="/icons/mouse.svg"
                                        alt=""
                                    />
                                    <Text px="xl" color="gray">
                                        scroll below
                                    </Text>
                                </Grid.Col>
                            </Grid>
                        </Title>
                    </>
                ) : (
                    <></>
                )}
            </BackgroundImage>
        </Box>
    );
});

export default MainHeroSlide;
