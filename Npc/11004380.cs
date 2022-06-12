using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004380: Rufina
/// </summary>
public class _11004380 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;40
    }

    // Select 0:
    // $script:1109213607011795$
    // - You won't know love if you don't express it. Confess your love to your crush for the holidays! It's the perfect gift!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011796$
                // - The holidays are all about looooove.
                switch (selection) {
                    // $script:1109213607011797$
                    // - ...
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109213607011798$
                // - I have a pair of skates I really love... so much so that I don't want to take them out of the box.
                switch (selection) {
                    // $script:1109213607011799$
                    // - You skate with them still inside the box? Sounds kind of dangerous.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109213607011800$
                // - No way! I've never even worn them! I wonder what it'd be like to skate with them... Maybe that's what love is, taking risks.
                return -1;
            case (40, 0):
                // $script:1120173007011871$
                // - The holidays are all about looooove.
                switch (selection) {
                    // $script:1120173007011872$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1120173007011873$
                // - I know $npcName:11004348[gender:0]$, he's $npcName:11004345[gender:1]$'s father. I saw him last night at the gardening club meeting. But I didn't see him today. I bet he's just at home... He mentioned wanting to decorate his holiday tree.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
