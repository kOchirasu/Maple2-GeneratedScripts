using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000745: Ghanush
/// </summary>
public class _11000745 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;60
    }

    // Select 0:
    // $script:0831180407002891$
    // - Do you think you can beat me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002894$
                // - Do you want to challenge me? You know how to play rock-paper-scissors, right? Heh, let's do it. Rock, paper, scissors!
                switch (selection) {
                    // $script:0831180407002895$
                    // - Scissors!
                    case 0:
                        // TODO: goto 31,32,33,34,35
                        return -1;
                    // $script:0831180407002896$
                    // - Rock!
                    case 1:
                        // TODO: goto 36,37,38,39,40
                        return -1;
                    // $script:0831180407002897$
                    // - Paper!
                    case 2:
                        // TODO: goto 41,42,43,44,45
                        return -1;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002898$
                // - <font color="#909090">(She plays scissors.)</font>
                //   We tied. Not bad. Do you want to try again?
                switch (selection) {
                    // $script:0831180407002899$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (32, 0):
                // $script:0831180407002900$
                // - <font color="#909090">(She plays scissors.)</font>
                //   We tied. Why don't you try again?
                switch (selection) {
                    // $script:0831180407002901$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (33, 0):
                // $script:0831180407002902$
                // - <font color="#909090">(She plays rock.)</font>
                //   I won. Looks like you're no match for me either.
                switch (selection) {
                    // $script:0831180407002903$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (34, 0):
                // $script:0831180407002904$
                // - <font color="#909090">(She plays rock.)</font>
                //   I won. What's wrong, cat got your tongue? Oh, right... losers don't get to speak! Hee hee... Want to play again?
                switch (selection) {
                    // $script:0831180407002905$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (35, 0):
                // $script:0831180407002906$
                // - <font color="#909090">(She plays paper.)</font>
                //   Oh no, I lost! I can't believe it!
                switch (selection) {
                    // $script:0831180407002907$
                    // - I won!
                    case 0:
                        return 46;
                }
                return -1;
            case (36, 0):
                // $script:0831180407002908$
                // - <font color="#909090">(She plays scissors.)</font>
                //   D-did I really just lose?
                switch (selection) {
                    // $script:0831180407002909$
                    // - I won!
                    case 0:
                        return 46;
                }
                return -1;
            case (37, 0):
                // $script:0831180407002910$
                // - <font color="#909090">(She plays rock.)</font>
                //   We tied. This isn't over. Let's go again!
                switch (selection) {
                    // $script:0831180407002911$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (38, 0):
                // $script:0831180407002912$
                // - <font color="#909090">(She plays rock.)</font>
                //   We tied. Not bad. Do you want to try again?
                switch (selection) {
                    // $script:0831180407002913$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (39, 0):
                // $script:0831180407002914$
                // - <font color="#909090">(She plays paper.)</font>
                //   I won. Seems I can't find a good match for me here, either. Do you want to try again?
                switch (selection) {
                    // $script:0831180407002915$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (40, 0):
                // $script:0831180407002916$
                // - <font color="#909090">(She plays paper.)</font>
                //   I'm tired of winning. I'm willing to play you one more time, though. What do you say?
                switch (selection) {
                    // $script:0831180407002917$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002918$
                // - <font color="#909090">(She plays scissors.)</font>
                //   I won. As expected. Do you want to try again?
                switch (selection) {
                    // $script:0831180407002919$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (42, 0):
                // $script:0831180407002920$
                // - <font color="#909090">(She plays scissors.)</font>
                //   Ahhh... Winning doesn't excite me anymore. Do you want to try again?
                switch (selection) {
                    // $script:0831180407002921$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (43, 0):
                // $script:0831180407002922$
                // - <font color="#909090">(She plays rock.)</font>
                //   N-no way... D-did I really lose?
                switch (selection) {
                    // $script:0831180407002923$
                    // - Again!
                    case 0:
                        return 46;
                }
                return -1;
            case (44, 0):
                // $script:0831180407002924$
                // - <font color="#909090">(She plays paper.)</font>
                //   Err? We tied. Let's try again!
                switch (selection) {
                    // $script:0831180407002925$
                    // - Again!
                    case 0:
                        return 50;
                }
                return -1;
            case (45, 0):
                // $script:0831180407002926$
                // - <font color="#909090">(She plays paper.)</font>
                //   Hmph, tying is no fun. Let's try again.
                switch (selection) {
                    // $script:0831180407002927$
                    // - Yes!
                    case 0:
                        return 50;
                }
                return -1;
            case (46, 0):
                // $script:0831180407002928$
                // - <font color="#909090">(She gives you a sideways scowl.)</font> 
                //   I think you played after I did. You're lucky that my eyes are too old to see clearly.
                switch (selection) {
                    // $script:0831180407002929$
                    // - Don't you have something for me?
                    case 0:
                        // TODO: goto 47,48
                        // TODO: gotoFail 49
                        return -1;
                }
                return -1;
            case (47, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002930$
                // - <font color="#909090">(Her scowl deepens.)</font>
                //   Here!
                return -1;
            case (48, 0):
                // $script:0831180407002931$
                // - I already gave you your prize!
                return -1;
            case (49, 0):
                // $script:0831180407002932$
                // - You'd better lighten your bag first if you want a prize.
                return -1;
            case (50, 0):
                // $script:0831180407002933$
                // - Let's get to it! Rock, paper, scissors!
                switch (selection) {
                    // $script:0831180407002934$
                    // - Scissors!
                    case 0:
                        // TODO: goto 31,32,33,34,35
                        return -1;
                    // $script:0831180407002935$
                    // - Rock!
                    case 1:
                        // TODO: goto 36,37,38,39,40
                        return -1;
                    // $script:0831180407002936$
                    // - Paper!
                    case 2:
                        // TODO: goto 41,42,43,44,45
                        return -1;
                }
                return -1;
            case (60, 0):
                // $script:0831180407002937$
                // - Do you know how to play rock-paper-scissors? It's a little more complex than making funny shapes with your hand.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.SelectableDistractor,
            (37, 0) => NpcTalkButton.SelectableDistractor,
            (38, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.SelectableDistractor,
            (44, 0) => NpcTalkButton.SelectableDistractor,
            (45, 0) => NpcTalkButton.SelectableDistractor,
            (46, 0) => NpcTalkButton.SelectableDistractor,
            (47, 0) => NpcTalkButton.Close,
            (48, 0) => NpcTalkButton.Close,
            (49, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
