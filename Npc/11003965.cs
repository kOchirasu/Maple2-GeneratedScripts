using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003965: Soul Binder
/// </summary>
public class _11003965 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010021$
    // - What a wondrous place.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010022$
                // - This place is beautiful. Don't you agree?
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
