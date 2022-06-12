using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001342: Venchas
/// </summary>
public class _11001342 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005288$
    // - Sigh... This is getting tiring...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005291$
                // - You can't swat a bug in the water, but you can still spray it.
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
