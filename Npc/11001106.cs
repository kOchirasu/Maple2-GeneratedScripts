using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001106: Redanis
/// </summary>
public class _11001106 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003715$
    // - W-what?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003718$
                // - I'm not completely healed, but I'm in much better shape than I was when I first arrived. I should be able to go back to my family soon. 
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
