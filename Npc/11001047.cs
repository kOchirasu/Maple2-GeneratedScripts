using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001047: Reker
/// </summary>
public class _11001047 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003578$
    // - This has been a perfect misjudgment.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003581$
                // - Everyone at  Goldus Industries is a real smooth talker. They say they care about us workers, but if they did we wouldn't be having any problems, would we?
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
