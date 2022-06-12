using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000341: Rue
/// </summary>
public class _11000341 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001367$
    // - Did you come to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001370$
                // - After my family fell, the only thing I had left was the mansion. I decided to forget my former glory as the heiress of House Andrea, and turned the mansion into $map:02000178$. People started to call me $npcName:11000341[gender:1]$ not long after.
                return 30;
            case (30, 1):
                // $script:0831180407001371$
                // - $npcName:11000340[gender:0]$ had been the butler for my family as long as I could remember. When my family fell, he stayed behind when everyone else left. Now he's the hotelier of my hotel. I owe him so much.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
