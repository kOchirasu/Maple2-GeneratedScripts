using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000359: Hendel
/// </summary>
public class _11000359 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001489$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001491$
                // - Are you traveling? You look like you're about my son's age.
                return 20;
            case (20, 1):
                // $script:0831180407001492$
                // - $npcName:11000360[gender:0]$ is my only child. He left home recently, wanting to strike out on his own. If only he knew how much that hurt his mother.
                return 20;
            case (20, 2):
                // $script:0831180407001493$
                // - The day before yesterday I got a letter from $npcName:11000360[gender:0]$. He must've written it somewhere around here... even the edges are singed. So I bought an ice pack to keep him cool.
                return 20;
            case (20, 3):
                // $script:0831180407001494$
                // - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
                return -1;
            case (30, 0):
                // $script:0831180407001495$
                // - My son, $npcName:11000360[gender:0]$ is on the other side of all that lava. I wanted to visit him, but I'm just too scared to cross it myself.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
