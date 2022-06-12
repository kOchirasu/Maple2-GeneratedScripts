using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000697: Blind Rio
/// </summary>
public class _11000697 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002813$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002816$
                // - Mm... Who's there? I can't see you, but I can sense your burning soul.
                switch (selection) {
                    // $script:0831180407002817$
                    // - What happened?
                    case 0:
                        return 51;
                    // $script:0831180407002818$
                    // - What's the $map:65000002$?
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407002819$
                // - ...Do you mean my eyes? As you can see, I'm blind. I committed a sin so grave that I gave up my eyes in penance.
                return 51;
            case (51, 1):
                // $script:0831180407002820$
                // - I can tell you want to hear my story. I assume $npcName:11000289[gender:0]$ told you about the arena. That is where you can always find a fair fight. No battles to the death, just competitions of strength.
                return 51;
            case (51, 2):
                // $script:0831180407002821$
                // - But I killed someone there. It was an accident, and everyone who watched our fight agreed that it was unavoidable, but I couldn't forgive myself.
                return 51;
            case (51, 3):
                // $script:0831180407002822$
                // - That's why I decided to hide in the darkness. That's all.
                return -1;
            case (52, 0):
                // $script:0831180407002823$
                // - You must be interested in the $map:65000002$. But as its name suggests, it's a dangerous place. Everyone in there is determined to hurt each other in a contest of strength. If you want to join in, you'd better prepare well.
                return 52;
            case (52, 1):
                // $script:0831180407002824$
                // - The $map:65000002$ is a battleground in which up to 10 warriors battle each other for points, and whoever beats more competitors than the others wins. When you beat another warrior, you get points. When you are beaten, you lose them.
                return 52;
            case (52, 2):
                // $script:0831180407002825$
                // - Since so many warriors fight each other at the same time, sometimes things get really chaotic. The winner might not be the strongest of them all, but the smartest.
                return 52;
            case (52, 3):
                // $script:0831180407002826$
                // - It's always good to test your strength, but be careful not to let your excitement get the best of you. That's all I have to tell you. Be on your way.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Next,
            (51, 2) => NpcTalkButton.Next,
            (51, 3) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.Next,
            (52, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
