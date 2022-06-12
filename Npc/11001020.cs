using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001020: Clarke
/// </summary>
public class _11001020 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003467$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003709$
                // - I can feel time being restored to order. This means there isn't much of it left for us to spend together.
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
