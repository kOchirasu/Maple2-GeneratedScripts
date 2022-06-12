using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000632: Jimmy
/// </summary>
public class _11000632 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;60
    }

    // Select 0:
    // $script:0831180407002549$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002553$
                // - You're touring $map:02000124$, are you? Stick to the route, then. You wouldn't want to mess with some of these prisoners.
                switch (selection) {
                    // $script:0831180407002554$
                    // - What kinds of offenses have these prisoners committed?
                    case 0:
                        return 41;
                    // $script:0831180407002555$
                    // - Can they get their sentences reduced?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002556$
                // - They've spoken lies or slander about certain people or places, publicly supported or attacked public groups, or used chat, displays, UGC, or character names to offend others.
                return 41;
            case (41, 1):
                // $script:0831180407002557$
                // - Of course, one doesn't get thrown into prison for committing these offenses just once. They're given multiple chances to redeem themselves first. If they still refuse to see the error of their ways and keep making the same mistakes, then they will receive punishment from $npcTitle:11000514[gender:1]$ and Judge $npcName:11000514[gender:1]$.
                return -1;
            case (42, 0):
                // $script:0831180407002558$
                // - $npcName:11000514[gender:1]$'s punishment can make their life in Maple World very difficult. But if they prove how sorry they are, they can have their sentence reduced.
                return 42;
            case (42, 1):
                // $script:0831180407002559$
                // - Pulling weeds in the prison yard is one way of proving that, but so far I haven't seen any prisoner pull weeds long enough to have their sentence reduced. It just proves that some people don't change.
                return -1;
            case (50, 0):
                // functionID=1 
                // $script:0831180407002560$
                // - For more information about the prison, please refer to this brochure. Enjoy your tour.
                return -1;
            case (60, 0):
                // $script:0831180407002561$
                // - You already have a $item:39000009$. I hope it'll help guide you around $map:02000124$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
