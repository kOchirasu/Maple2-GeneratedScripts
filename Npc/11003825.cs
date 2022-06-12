using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003825: Tristan
/// </summary>
public class _11003825 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0115140307009749$
    // - Let's get to business.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0115140307009750$
                // - ...Finally, the time has come.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
