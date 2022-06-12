using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001144: Machias
/// </summary>
public class _11001144 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0915220707003955$
    // - Come closer! Yes, you my child.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915220707003958$
                // - To picture the future clearly, I must make myself one with nature. Focus your senses. The breeze carries with it the scent of flowers. The waterfall quietly roars.
                return 30;
            case (30, 1):
                // $script:0915222107003979$
                // - For an accurate reading, I must focus my mind and keep disruptive thoughts at bay.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
