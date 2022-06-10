using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000745: Ghanush
/// </summary>
public class _11000745 : NpcScript {
    internal _11000745(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002891$ 
                // - Do you think you can beat me? 
                return true;
            case 30:
                // $script:0831180407002894$ 
                // - Do you want to challenge me? You know how to play rock-paper-scissors, right? Heh, let's do it. Rock, paper, scissors! 
                switch (selection) {
                    // $script:0831180407002895$
                    // - Scissors!
                    case 0:
                        Id = 0; // TODO: 31,32,33,34,35 | 
                        return false;
                    // $script:0831180407002896$
                    // - Rock!
                    case 1:
                        Id = 0; // TODO: 36,37,38,39,40 | 
                        return false;
                    // $script:0831180407002897$
                    // - Paper!
                    case 2:
                        Id = 0; // TODO: 41,42,43,44,45 | 
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002898$ 
                // - <font color="#909090">(She plays scissors.)</font>
We tied. Not bad. Do you want to try again? 
                switch (selection) {
                    // $script:0831180407002899$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407002900$ 
                // - <font color="#909090">(She plays scissors.)</font>
We tied. Why don't you try again? 
                switch (selection) {
                    // $script:0831180407002901$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407002902$ 
                // - <font color="#909090">(She plays rock.)</font>
I won. Looks like you're no match for me either. 
                switch (selection) {
                    // $script:0831180407002903$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 34:
                // $script:0831180407002904$ 
                // - <font color="#909090">(She plays rock.)</font>
I won. What's wrong, cat got your tongue? Oh, right... losers don't get to speak! Hee hee... Want to play again? 
                switch (selection) {
                    // $script:0831180407002905$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 35:
                // $script:0831180407002906$ 
                // - <font color="#909090">(She plays paper.)</font>
Oh no, I lost! I can't believe it! 
                switch (selection) {
                    // $script:0831180407002907$
                    // - I won!
                    case 0:
                        Id = 46;
                        return false;
                }
                return true;
            case 36:
                // $script:0831180407002908$ 
                // - <font color="#909090">(She plays scissors.)</font>
D-did I really just lose? 
                switch (selection) {
                    // $script:0831180407002909$
                    // - I won!
                    case 0:
                        Id = 46;
                        return false;
                }
                return true;
            case 37:
                // $script:0831180407002910$ 
                // - <font color="#909090">(She plays rock.)</font>
We tied. This isn't over. Let's go again! 
                switch (selection) {
                    // $script:0831180407002911$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 38:
                // $script:0831180407002912$ 
                // - <font color="#909090">(She plays rock.)</font>
We tied. Not bad. Do you want to try again? 
                switch (selection) {
                    // $script:0831180407002913$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 39:
                // $script:0831180407002914$ 
                // - <font color="#909090">(She plays paper.)</font>
I won. Seems I can't find a good match for me here, either. Do you want to try again? 
                switch (selection) {
                    // $script:0831180407002915$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 40:
                // $script:0831180407002916$ 
                // - <font color="#909090">(She plays paper.)</font>
I'm tired of winning. I'm willing to play you one more time, though. What do you say? 
                switch (selection) {
                    // $script:0831180407002917$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002918$ 
                // - <font color="#909090">(She plays scissors.)</font>
I won. As expected. Do you want to try again? 
                switch (selection) {
                    // $script:0831180407002919$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407002920$ 
                // - <font color="#909090">(She plays scissors.)</font>
Ahhh... Winning doesn't excite me anymore. Do you want to try again? 
                switch (selection) {
                    // $script:0831180407002921$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 43:
                // $script:0831180407002922$ 
                // - <font color="#909090">(She plays rock.)</font>
N-no way... D-did I really lose? 
                switch (selection) {
                    // $script:0831180407002923$
                    // - Again!
                    case 0:
                        Id = 46;
                        return false;
                }
                return true;
            case 44:
                // $script:0831180407002924$ 
                // - <font color="#909090">(She plays paper.)</font>
Err? We tied. Let's try again! 
                switch (selection) {
                    // $script:0831180407002925$
                    // - Again!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 45:
                // $script:0831180407002926$ 
                // - <font color="#909090">(She plays paper.)</font>
Hmph, tying is no fun. Let's try again. 
                switch (selection) {
                    // $script:0831180407002927$
                    // - Yes!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 46:
                // $script:0831180407002928$ 
                // - <font color="#909090">(She gives you a sideways scowl.)</font> 
I think you played after I did. You're lucky that my eyes are too old to see clearly. 
                switch (selection) {
                    // $script:0831180407002929$
                    // - Don't you have something for me?
                    case 0:
                        Id = 0; // TODO: 47,48 | 49
                        return false;
                }
                return true;
            case 47:
                // $script:0831180407002930$ functionID=1 
                // - <font color="#909090">(Her scowl deepens.)</font>
Here! 
                return true;
            case 48:
                // $script:0831180407002931$ 
                // - I already gave you your prize! 
                return true;
            case 49:
                // $script:0831180407002932$ 
                // - You'd better lighten your bag first if you want a prize. 
                return true;
            case 50:
                // $script:0831180407002933$ 
                // - Let's get to it! Rock, paper, scissors! 
                switch (selection) {
                    // $script:0831180407002934$
                    // - Scissors!
                    case 0:
                        Id = 0; // TODO: 31,32,33,34,35 | 
                        return false;
                    // $script:0831180407002935$
                    // - Rock!
                    case 1:
                        Id = 0; // TODO: 36,37,38,39,40 | 
                        return false;
                    // $script:0831180407002936$
                    // - Paper!
                    case 2:
                        Id = 0; // TODO: 41,42,43,44,45 | 
                        return false;
                }
                return true;
            case 60:
                // $script:0831180407002937$ 
                // - Do you know how to play rock-paper-scissors? It's a little more complex than making funny shapes with your hand. 
                return true;
            default:
                return true;
        }
    }
}
