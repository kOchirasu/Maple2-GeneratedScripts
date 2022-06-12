using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000217: Candice
/// </summary>
public class _11000217 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000947$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000949$
                // - I grew up in $map:02000084$, that's where my family lives. I heard about a job that paid well, so I moved all the way here.
                return 20;
            case (20, 1):
                // $script:0831180407000950$
                // - All I had to do was look after some rich guy's son. Man was that a mistake. This kid I'm looking after treats me worse than his cat.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
