using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000958: Ruman
/// </summary>
public class _11000958 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003319$
    // - Aww, my poor scaredy-cats!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003321$
                // - My babies are as precious as children to me. Hee hee.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
