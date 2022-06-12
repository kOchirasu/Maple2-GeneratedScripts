using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000526: Raymon
/// </summary>
public class _11000526 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002247$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002250$
                // - I need to find a better place to hide. The Dark Wind would have no trouble finding me here.
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
