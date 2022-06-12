using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001098: Moif
/// </summary>
public class _11001098 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003693$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003696$
                // - Hey, hey! This place is dangerous. Get out of here! We don't need you fouling up any of the valves.
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
