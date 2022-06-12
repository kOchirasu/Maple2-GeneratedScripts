using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003957: Thief
/// </summary>
public class _11003957 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010005$
    // - Eh? You...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010006$
                // - Are you here casing the joint? I've got dibs, alright?!
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
