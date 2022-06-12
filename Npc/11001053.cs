using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001053: Houzin
/// </summary>
public class _11001053 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003596$
    // - My emotions got the best of me. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003599$
                // - The greatest martial artists aren't always the strongest ones. They're the ones who are humble and always put other people first. 
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
