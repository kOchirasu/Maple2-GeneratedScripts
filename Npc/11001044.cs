using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001044: Papa Santa
/// </summary>
public class _11001044 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003565$
    // - I'm the messenger of hopes and dreams! Why is this happening to me? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003568$
                // - I like being a Santa. How could I not? I'm giving people joy!
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
