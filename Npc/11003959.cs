using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003959: Berserker
/// </summary>
public class _11003959 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010009$
    // - Who're you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010010$
                // - You look pretty tough! Up for a sparring match?
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
