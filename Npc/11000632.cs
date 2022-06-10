using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000632: Jimmy
/// </summary>
public class _11000632 : NpcScript {
    internal _11000632(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002549$ 
                // - How may I help you? 
                return true;
            case 40:
                // $script:0831180407002553$ 
                // - You're touring $map:02000124$, are you? Stick to the route, then. You wouldn't want to mess with some of these prisoners. 
                switch (selection) {
                    // $script:0831180407002554$
                    // - What kinds of offenses have these prisoners committed?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002555$
                    // - Can they get their sentences reduced?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002556$ 
                // - They've spoken lies or slander about certain people or places, publicly supported or attacked public groups, or used chat, displays, UGC, or character names to offend others. 
                // $script:0831180407002557$ 
                // - Of course, one doesn't get thrown into prison for committing these offenses just once. They're given multiple chances to redeem themselves first. If they still refuse to see the error of their ways and keep making the same mistakes, then they will receive punishment from $npcTitle:11000514[gender:1]$ and Judge $npcName:11000514[gender:1]$. 
                return true;
            case 42:
                // $script:0831180407002558$ 
                // - $npcName:11000514[gender:1]$'s punishment can make their life in Maple World very difficult. But if they prove how sorry they are, they can have their sentence reduced. 
                // $script:0831180407002559$ 
                // - Pulling weeds in the prison yard is one way of proving that, but so far I haven't seen any prisoner pull weeds long enough to have their sentence reduced. It just proves that some people don't change. 
                return true;
            case 50:
                // $script:0831180407002560$ functionID=1 
                // - For more information about the prison, please refer to this brochure. Enjoy your tour. 
                return true;
            case 60:
                // $script:0831180407002561$ 
                // - You already have a $item:39000009$. I hope it'll help guide you around $map:02000124$. 
                return true;
            default:
                return true;
        }
    }
}
