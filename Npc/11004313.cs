using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004313: Condor
/// </summary>
public class _11004313 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0928133807011352$
    // - Back in my day, we knew a thing or two about duty!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0928133807011353$
                // - I'm here, but most of my men are tied up defending Victoria Island. I hate being benched!
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
