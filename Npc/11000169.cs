using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000169: Mark
/// </summary>
public class _11000169 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;70
    }

    // Select 0:
    // $script:0831180407000700$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000704$
                // - $MyPCName$, do I look timid to you?
                switch (selection) {
                    // $script:0831180407000705$
                    // - Maybe... a little?
                    case 0:
                        return 51;
                    // $script:0831180407000706$
                    // - Not at all.
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407000707$
                // - I do, huh? Ahh, no wonder! Miss $npcName:11000160[gender:1]$ said she doesn't like timid men. What should I do?
                return -1;
            case (52, 0):
                // $script:0831180407000708$
                // - Are you sure? I do hope Miss $npcName:11000160[gender:1]$ thinks the same of me, $MyPCName$. If that's the case, I might actually have a shot.
                return -1;
            case (70, 0):
                // $script:0831180407000709$
                // - It's not easy to stand in one spot all day guarding the arsenal, but someone has to do it. I'm proud of my job, too.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
