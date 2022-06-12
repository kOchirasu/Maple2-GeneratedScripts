using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001513: Paulie
/// </summary>
public class _11001513 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0419105410001487$
    // - How may I help you look amazing?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0420153110001493$
                // - Looking for some head-turning hair? Then you came to the right place, $MyPCName$. My special hairstyles are unmatched!
                switch (selection) {
                    // $script:0420153110001494$
                    // - I leave my special hairstyle to you, maestro.
                    case 0:
                        return 0;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}
