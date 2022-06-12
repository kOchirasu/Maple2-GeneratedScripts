using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000848: Phelan
/// </summary>
public class _11000848 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003103$
    // - What is it? I'm doing something really important. Please don't distract me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003106$
                // - The world keeps changing, and our technology and science leads the way. Mark my words, I'll usher in a new era with my work. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
